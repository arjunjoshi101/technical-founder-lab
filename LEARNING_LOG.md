# Learning Log

## Day 1 — 23 September 2026

### Completed

- verified Git
- configured Git identity
- created `~/Projects/technical-founder-lab`
- initialised repository
- created README
- learned untracked → staged → committed
- created first commit `7315dfb`
- installed Homebrew
- installed GitHub CLI
- authenticated GitHub
- created public GitHub repo
- configured `origin`
- pushed `main`
- connected Codex to the repository

### Learning mistakes

- accidentally attempted to execute a directory path as a command
- accidentally pasted Git commands into README.md

### Day 1 completion — Git workflow and persistent project setup

- Created and pushed a feature branch
- Inspected staged changes
- Created a pull request
- Reviewed it
- Merged it into main
- Deleted the remote feature branch
- Synchronised local main
- Created a dedicated ChatGPT Project called Technical Founder Sprint and added persistent Project Instructions
- Completed Day 1's Git workflow; Day 1 status: **Complete**

Next action: **Begin Day 2: understand the architecture and data flow of a modern web application before writing application code.**

## Day 2 — 25 September 2026

Status: **Complete**

### Completed

- Learned browser vs frontend
- Learned frontend vs backend
- Learned backend vs database
- Learned API vs HTTP
- Learned JSON as a structured data exchange format
- Learned authentication vs authorisation
- Learned why third-party API keys belong in the backend
- Learned deployment vs localhost
- Learned Uvicorn vs FastAPI
- Built and ran a minimal FastAPI + HTML/JavaScript application
- Observed a real `POST /api/search` request in Chrome DevTools
- Inspected the JSON request payload and JSON response
- Observed `200 OK` and `404 Not Found`
- Deliberately stopped Uvicorn and observed `connection refused`
- Proved the current search logic is hard-coded by sending an unrelated query and receiving the same results

### Project files

- `day-02-web-flow/app.py`
- `day-02-web-flow/static/index.html`
- `day-02-web-flow/requirements.txt`

### Debugging and learning moments

- Accidentally used a trailing backslash in a `cd` command, causing the next command to be joined to the path
- Learned that code existing on disk is not the same thing as a running server
- Initially conflated FastAPI/backend/database and clarified those boundaries

Next action: **Begin Day 3: transform the Day 2 request flow into an LLM-powered Program Extractor that takes messy university programme text and returns structured JSON.**

### Day 2 Git completion — 25 September 2026

- Added `.gitignore` rules for Python caches, virtual environments and environment secrets, with an exception for `.env.example`
- Reviewed the changes, staged the intended files and inspected the staged diff
- Created commit `8f3da95 — feat: add Day 2 web request flow demo` and pushed the Day 2 branch
- Created and reviewed PR #3, then merged it into `main` as merge commit `6ef526d`
- Deleted the remote `day2-web-request-flow` branch, checked out local `main`, pulled and verified a clean working directory before this learning-record update
- Day 2 learning and Git workflow are complete; Day 3 implementation has not started

Next action: **Define the Program Extractor's input, output fields, and request flow before implementation.**
