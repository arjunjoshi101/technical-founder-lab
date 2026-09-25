from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI()
HTML_FILE = Path(__file__).parent / "static" / "index.html"


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=500)


@app.get("/")
def home():
    # Serve the frontend from the same server as the API.
    return FileResponse(HTML_FILE)


@app.post("/api/search")
def search(request: SearchRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=422, detail="Please enter a query.")

    print(f"Received search query: {query}", flush=True)

    # Fictional examples: every valid query returns the same three programmes.
    # FastAPI converts this Python dictionary into a JSON response.
    return {
        "programmes": [
            {"university": "Northbridge University", "title": "Master of Public Policy", "country": "UK"},
            {"university": "Westhaven University", "title": "MSc Social and Public Policy", "country": "UK"},
            {"university": "Kingsmere University", "title": "MA Governance and Public Policy", "country": "UK"},
        ]
    }
