# Learning State

- Current day: Day 2
- Date: 25 September 2026
- Status: **Day 2 learning complete; Git closure pending**
- Git version verified: 2.50.1 Apple Git-155
- Git identity configured as Arjun Joshi
- Local repo: `/Users/arjunjoshi/Projects/technical-founder-lab`
- GitHub repo: `arjunjoshi101/technical-founder-lab`
- First commit: `7315dfb — docs: start technical founder lab`
- Codex successfully connected to the local repository
- GitHub remote successfully configured and first commit pushed

## Day 2 accomplishments

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

## Day 2 project files

- `day-02-web-flow/app.py`
- `day-02-web-flow/static/index.html`
- `day-02-web-flow/requirements.txt`

## Concepts encountered on Day 1

- repository
- working directory
- Git vs GitHub
- `.git`
- untracked file
- staging area
- commit
- commit hash
- branch
- main
- remote
- origin
- push
- staged diff
- pull request
- review
- merge
- remote branch deletion
- pull and local main synchronisation

## Day 1 completed workflow

- Created and pushed a feature branch
- Inspected staged changes
- Created a pull request
- Reviewed it
- Merged it into main
- Deleted the remote feature branch
- Synchronised local main
- Created a dedicated ChatGPT Project called Technical Founder Sprint and added persistent Project Instructions

## Still to complete on Day 2

Day 2's learning and practical exercises are complete. Git closure is pending: review the changes, stage the intended files, inspect the staged diff, commit, push, create and review a pull request, merge, return to main, pull and verify a clean state.

Before staging, exclude generated Python cache files from the change set. The review found `day-02-web-flow/__pycache__/app.cpython-313.pyc` untracked and not ignored.

## Next action

**review → stage → inspect staged diff → commit → push → PR → review → merge → checkout main → pull → verify clean state.**

## After Day 2 Git closure

**Begin Day 3: transform the Day 2 request flow into an LLM-powered Program Extractor that takes messy university programme text and returns structured JSON.**
