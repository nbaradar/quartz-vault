---
title: Python Testing
tags:
  - reference
  - python
  - testing
draft:
created: 2025-10-28

modified: 2025-10-28
published: 2025-10-28

---
# Overview
## Setup
First create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
OR w/ `uv`
```bash
uv venv
source .venv/bin/activate
```

Then install project dependencies:
```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio
```

## Running Tests
Then run the specific test file.... 
### Verbose Mode
```bash
pytest tests/test_tag_search.py -v
```

### Run only Unit Tests
```bash
pytest -k "not integration and not slow" -q
```

### Run all tests except slow
```bash
pytest -m "not slow" -v
```

### Run only integration tests
```bash
pytest -m integration -v
```

### Run a single test function inside the test file
```bash
pytest tests/test_tag_search.py::TestTagSearchBasics::test_single_tag_match -q
```

# Report Options
3 Test Reporting libraries you could use:
- `pytest-html `
- `pytest-json-report `
- `pytest-cov`
## Console w/ verbose + show locals options
- Command: `pytest tests/test_tag_search.py -vv -r a --showlocals`
- Shows per-test output, full summary (fails, xfails, skips, warnings).
## Show slowest tests
- Command: `pytest tests/test_tag_search.py --durations=10`
- Shows the top 10 slowest tests (use 0 for all).
## Additional Libraries
- JUnit XML (CI friendly)
    - Command: pytest --junitxml=reports/junit.xml
    - Produces `reports/junit.xml` consumable by CI systems.
- HTML (human-friendly)
    - Command: pytest --html=reports/report.html --self-contained-html
    - Produces `reports/report.html` you can open in a browser.
- JSON programmatic report
    - Command: pytest --json-report --json-report-file=reports/report.json
    - Produces `reports/report.json` for automated parsing.
