# Learning State

- Current day: Day 2
- Date: 25 September 2026
- Status: **Day 2 learning and Git workflow complete**
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

## Day 2 Git completion

- Reviewed and staged the Day 2 changes, then inspected the staged diff
- Added `.gitignore` rules for generated Python caches, virtual environments and environment secrets, while allowing `.env.example`
- Created commit `8f3da95 — feat: add Day 2 web request flow demo`
- Pushed the Day 2 branch and created, reviewed and merged PR #3
- Merge commit: `6ef526d`
- Deleted the remote `day2-web-request-flow` branch
- Checked out local `main`, pulled the merged changes and verified a clean working directory before this learning-record update

## Day 3 status

Program Extractor implementation has not started.

## Next action

**Define the Program Extractor's input, output fields, and request flow before implementation.**
