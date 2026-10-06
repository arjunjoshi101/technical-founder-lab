# Technical Founder Programme — 30 Learning Sessions

The goal is to architect, build, inspect, debug, evaluate and operate useful agents through plain-English instructions. Learn the controls: Git, APIs, schemas, tests, logs, permissions, secrets, state, deployment, model limitations and cost.

“Days” below are learning sessions, not calendar deadlines. Preserve progress and repeat or extend a session when useful.

## Day 30 target

Demonstrate one small workflow: **phone instruction → agent → isolated Git branch → code change → tests → preview → human review and approval.** Diagnose a failure and explain the system, its boundaries and its limitations.

This is a scoped learning target, not guaranteed autonomy. The broader Setu GTM system remains a post-sprint objective.

## Principles

- Start with one agent; add multiple agents only for a clear need.
- AI coding agents are encouraged, but the founder must understand what is shipped.
- Every substantive feature should be inspected, tested and explainable.
- Important programme state belongs in files/Git rather than relying on chat context.
- Local open models and Ollama are a core track: memory, context, quantisation, speed, quality and licensing. Keep `qwen3:4b-instruct` as the initial extractor baseline.
- Use local inference for the extractor and the existing ChatGPT account for Codex. Do not introduce paid APIs now; verify supported access before committing to a remote coding-agent integration.
- Stored memory saves facts or state; evaluation-driven improvements change prompts, tools or rules based on results; fine-tuning trains model weights. Fine-tuning is optional later.
- Use SQL and deterministic rules for exact constraints. Keep Telegram separate from the core workflow so other interfaces can follow.
- External outreach requires explicit approval; drafting does not authorise sending. Human approval also remains part of the coding workflow.

## Programme

**Day 1 — Complete:** Git/GitHub foundations — repository, commit, staging, branches, remote, push/pull, PRs.

**Day 2 — Complete:** How modern applications work — browser, frontend, backend, API, database, model, deployment. Built and inspected the web request-flow demo.

**Day 3 — Learning checkpoint prepared; commit pending:** Program Extractor v0 — text input → local LLM → structured JSON. New-Mac setup, 12 offline tests, a live sample, browser request/response checks and a real 503 outage with functional recovery have evidence. The latest Northbridge screenshot is reported to show HTTP 200 and correct JSON; loading/disabled-button behaviour was not observed. The original recovery HTTP status remains unchecked. Deadline fabrication and currency omission remain unresolved. Preserve all historical evidence; preparing a checkpoint does not mean every check passed or Git closure is complete.

## Accelerated sequence — agreed 6 October 2026

The next session builds a useful local notes agent. Learn controls inside working tools, while carrying forward the extractor's recorded failures and missing observations. Do not repeat recent verification without a changed component or concrete concern. The previous schedule remains in the learning log.

**Day 4 — Local lab agent:** Build one small agent over an explicit selection of project notes using `search_notes`, `read_evidence` and `save_draft`. First task: draft a summary of Day 3 failures with file/line evidence. Start with the installed local baseline; verify its tool-request behaviour rather than assuming reliable tool use. Keep the core independent of the interface. Allow only selected reads and confined draft writes; validate arguments and prevent overwrites. Bound execution and expose each tool call, result, error, duration and stop reason in a local log. Check source references and one denied action before calling the demo successful.

**Day 5 — Background inbox worker:** Feed local queued requests into the same core, with one worker processing one job at a time. Persist queued/running/completed/failed states, job IDs and tool logs; bound retries and handle restart/duplicate jobs without duplicating draft writes. Start and stop the worker explicitly. This is a local file inbox, not an email integration or permission to send messages.

**Day 6 — Measured model comparison:** Use fixed notes-agent tasks and the recorded extractor failures to compare `qwen3:4b-instruct` with one suitable local alternative when its download is authorised. Record hardware, versions/settings, memory, context, quantisation, licensing, speed, tool-call validity and factual quality. Distinguish schema validity, supported facts, omissions and rejections. Preserve D3-ADV-001, D3-EVAL-002 and both historical deadline failures; no new model download is authorised by this curriculum edit.

**Day 7 — Coding worker:** Define one small repository task with acceptance criteria and verify the supported Codex CLI/account route. Work on an isolated branch or checkout, with bounded file/command permissions and an observable log. An installed CLI alone does not verify authentication or unattended execution. Keep the original checkout and unrelated changes safe.

**Day 8 — Coding tests and inspection:** Inspect the coding worker's diff, run relevant tests and diagnose a controlled failure from logs. Preserve the relationship between task, exact code revision, test result and worker state.

**Day 9 — Preview and human approval:** Produce a reviewable preview tied to the code revision and tests. Exercise approval, rejection and revision; successful tests or a preview do not authorise merging or publishing.

**Day 10 — Phone interface:** Add a thin Telegram adapter to the separate core workflow. Authenticate the sender and protect credentials before accepting phone-triggered jobs. Begin with the bounded notes task; keep the core invocable locally without Telegram. No external outreach without explicit approval.

**Day 11 — Phone job control:** Show job status, tool activity, evidence and drafts; support cancellation and explicit approval for consequential actions. Reject malformed or duplicate messages and test an unauthorised sender.

**Day 12 — Phone-to-coding rehearsal:** Connect one scoped coding task through branch, tests and preview to human review. Inspect failure and recovery across the interface/core boundary. Use only a verified supported coding integration; document any access limitation.

**Day 13 — Controlled operation/deployment:** Inspect who can invoke the worker, service start/stop, logs, secret configuration and local resource cost. Decide whether local operation suffices; any remote deployment or public exposure needs its own authorised scope. Check access and restart behaviour.

**Day 14 — Durable state:** Extend the working inbox to a small database where useful; inspect its schema, transitions and what survives a restart. Distinguish stored memory from model training.

**Day 15 — Recovery and retries:** Test interrupted jobs, duplicate delivery, stale running jobs and bounded retries. Avoid repeating side effects; make recoverable and terminal errors visible.

**Day 16 — Permissions and secrets review:** Challenge the allowlist, path boundaries, tool arguments and approval gates. Treat source instructions as untrusted data; keep credentials out of prompts, logs and Git.

**Day 17 — Agent evaluation:** Build a small repeatable set of notes tasks covering missing evidence, conflicting notes, malformed tool requests, embedded instructions and budget exhaustion. Score valid execution separately from supported answers and useful drafts.

**Day 18 — Deterministic checks and extractor follow-up:** Revisit deadline/currency failures with the fixed cases before changing prompts or rules. Exercise missing browser observations, Westhaven source comparison and a controlled real stall/504 when relevant. Keep exact constraints deterministic and compare correct extractions, rejections and errors separately; do not erase unresolved cases.

**Day 19 — Local-model operation:** Inspect memory, context pressure, latency and quality under the actual worker workload. Explain quantisation, licensing and cost; remeasure only when settings or models change. Evaluation-driven changes are not fine-tuning; fine-tuning remains optional later.

**Day 20 — End-to-end control review:** Rehearse phone instruction → core → isolated coding work → tests → preview → human approval. Explain tool decisions, state, failure recovery and remaining limits; demonstrate rejection or revision.

**Day 21:** University RAG as a tool — collect a small public programme dataset with source URLs, dates and provenance; define the retrieval tool's input/output schema.

**Day 22:** Retrieval and citations — chunk and retrieve evidence, use metadata/SQL filters where exact constraints apply, and return grounded answers with citations through the core workflow.

**Day 23:** Retrieval evaluation — measure retrieval and answer support against a small known-answer set; test missing, conflicting and outdated evidence and abstention.

**Day 24:** Small Cohort Engine tool — create synthetic student data in SQL and define deterministic eligibility and capacity constraints.

**Day 25:** Deterministic scoring — rank eligible candidates using explicit, explainable preferences. Keep the model out of exact constraint decisions; test constraints and scoring.

**Day 26:** Tool integration — expose the small Cohort Engine through a schema, inspect its decisions and failures, and evaluate it on representative cases. Keep scope manageable for the final demonstration.

**Day 27:** Small Setu research-and-outreach-draft workflow — combine useful tools to produce sourced research and a draft for human review. External outreach requires explicit approval; the broader GTM system remains post-sprint work.

**Day 28:** Workflow evaluation and retries — evaluate research support and draft quality; add bounded retries only for appropriate failures, prevent duplicate side effects and inspect time/resource cost and logs.

**Day 29:** Portfolio documentation — document architecture, setup, permissions, tests, evaluations, model choices, limitations and contribution attribution. Rehearse the scoped phone workflow and its failure path.

**Day 30:** Phone-operated demonstration — phone instruction → agent → isolated Git branch → code change → tests → preview → human review and approval. Diagnose a controlled failure and explain the system, model limitations, costs and remaining work.
