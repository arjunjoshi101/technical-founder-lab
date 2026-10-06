import json
import unittest
from unittest.mock import patch

from fastapi import HTTPException
from pydantic import ValidationError

import app


SAMPLE = {
    "university": "Northbridge Example University",
    "programme": "MSc in Public Policy",
    "country": "United Kingdom",
    "duration_months": 12,
    "tuition_amount": 18000,
    "tuition_currency": "GBP",
    "application_deadline": None,
}


def envelope(data):
    return json.dumps({"done": True, "message": {"content": json.dumps(data)}}).encode()


class ExtractorTests(unittest.TestCase):
    def test_input_boundaries(self):
        for text in ("", "   ", "x" * 1501, None, 123):
            with self.subTest(text_type=type(text).__name__), self.assertRaises(ValidationError):
                app.ExtractRequest(text=text)
        self.assertEqual(len(app.ExtractRequest(text="x" * 1500).text), 1500)

    def test_missing_input_is_rejected(self):
        with self.assertRaises(ValidationError):
            app.ExtractRequest.model_validate({})

    def test_every_output_field_accepts_null(self):
        data = {key: None for key in SAMPLE}
        self.assertEqual(app.Programme.model_validate_json(json.dumps(data)).model_dump(), data)

    def test_wrong_output_values_are_rejected(self):
        changes = [
            {"duration_months": "12"}, {"duration_months": True},
            {"duration_months": -1}, {"tuition_amount": -1},
            {"tuition_amount": "18000"}, {"tuition_amount": float("inf")},
            {"tuition_currency": "$"}, {"application_deadline": "2026-02-30"},
            {"extra_key": "unexpected"},
        ]
        for change in changes:
            with self.subTest(change=change), self.assertRaises(ValidationError):
                app.Programme.model_validate_json(json.dumps(SAMPLE | change))

    def test_missing_output_key_is_rejected(self):
        data = dict(SAMPLE)
        del data["application_deadline"]
        with self.assertRaises(ValidationError):
            app.Programme.model_validate_json(json.dumps(data))

    def test_complete_date_is_accepted(self):
        result = app.Programme.model_validate_json(json.dumps(SAMPLE | {"application_deadline": "2027-03-15"}))
        self.assertEqual(result.application_deadline.isoformat(), "2027-03-15")

    def test_success_and_local_model_request(self):
        with patch.object(app, "call_ollama", return_value=envelope(SAMPLE)) as call:
            result = app.extract(app.ExtractRequest(text="Fictional programme text"))
        self.assertEqual(result.model_dump(), SAMPLE)
        call.assert_called_once()
        payload = call.call_args.args[0]
        self.assertEqual(payload["model"], "qwen3:4b-instruct")
        self.assertFalse(payload["stream"])
        self.assertEqual(payload["options"], {"num_ctx": 2048, "num_predict": 512, "temperature": 0})
        self.assertEqual(set(payload["format"]["required"]), set(SAMPLE))
        self.assertFalse(payload["format"]["additionalProperties"])
        self.assertEqual(payload["messages"][1]["role"], "user")

    def test_invalid_model_responses_become_502_without_retry(self):
        responses = [
            b"not JSON", b"null", b"[]", b"{}", envelope({}),
            b'{"done":true,"message":{"content":"not JSON"}}',
            b'{"done":true,"message":{"content":null}}',
            b'{"done":false,"message":{"content":"{}"}}',
            json.dumps({"done": True, "done_reason": "length", "message": {"content": json.dumps(SAMPLE)}}).encode(),
        ]
        for response in responses:
            with self.subTest(response=response), patch.object(app, "call_ollama", return_value=response) as call:
                with self.assertRaises(HTTPException) as caught:
                    app.extract(app.ExtractRequest(text="Example"))
                self.assertEqual(caught.exception.status_code, 502)
                call.assert_called_once()

    def test_local_connection_and_single_request(self):
        with patch.object(app, "HTTPConnection") as factory:
            connection = factory.return_value
            connection.getresponse.return_value.status = 200
            connection.getresponse.return_value.read.return_value = envelope(SAMPLE)
            self.assertEqual(app.call_ollama({"model": app.MODEL}), envelope(SAMPLE))
        factory.assert_called_once_with("localhost", 11434, timeout=90)
        connection.request.assert_called_once()
        self.assertEqual(connection.request.call_args.args, ("POST", "/api/chat"))
        connection.close.assert_called_once()

    def test_unavailable_and_timeout_errors(self):
        for error, expected in [(ConnectionRefusedError(), 503), (TimeoutError(), 504)]:
            with self.subTest(error=type(error).__name__), patch.object(app, "HTTPConnection") as factory:
                connection = factory.return_value
                connection.request.side_effect = error
                with self.assertRaises(HTTPException) as caught:
                    app.call_ollama({})
                self.assertEqual(caught.exception.status_code, expected)
                connection.request.assert_called_once()
                connection.close.assert_called_once()

    def test_ollama_http_errors(self):
        for upstream, expected in [(404, 503), (400, 502), (500, 502), (302, 502)]:
            with self.subTest(status=upstream), patch.object(app, "HTTPConnection") as factory:
                factory.return_value.getresponse.return_value.status = upstream
                with self.assertRaises(HTTPException) as caught:
                    app.call_ollama({})
                self.assertEqual(caught.exception.status_code, expected)

    def test_oversized_ollama_response(self):
        with patch.object(app, "HTTPConnection") as factory:
            response = factory.return_value.getresponse.return_value
            response.status = 200
            response.read.return_value = b"x" * 65537
            with self.assertRaises(HTTPException) as caught:
                app.call_ollama({})
            self.assertEqual(caught.exception.status_code, 502)


if __name__ == "__main__":
    unittest.main()
