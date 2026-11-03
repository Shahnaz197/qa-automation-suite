# QA Automation Suite

End-to-end **UI** and **API** test automation framework built with **Python, pytest and Playwright**, with CI on GitHub Actions.

![Test Automation](../../actions/workflows/tests.yml/badge.svg)

## What's covered

| Layer | Target | Tests |
|-------|--------|-------|
| UI (Playwright) | [saucedemo.com](https://www.saucedemo.com) | login (valid / locked / invalid, parametrized), cart add/remove, sorting, full checkout, form validation |
| API (requests) | [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) | GET, filter, POST, PUT, DELETE, 404 handling, response-time check |

## Design

- **Page Object Model**: selectors and actions live in `pages/`, tests only describe behaviour.
- **Fixtures** (`conftest.py`): shared API session, reusable `logged_in_page` fixture.
- **Markers**: `smoke`, `ui`, `api` to run subsets.
- **Parametrization** for data-driven negative tests.
- **HTML report** generated at `reports/report.html`.
- **CI**: runs on every push/PR and uploads the report as an artifact.

## Project structure

```
pages/            page objects (login, inventory, cart, checkout)
tests/ui/         browser tests
tests/api/        REST API tests
conftest.py       fixtures
pytest.ini        markers + report config
.github/workflows CI pipeline
```

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                      # everything
pytest -m smoke             # quick sanity set
pytest -m api               # API only
pytest -m ui --headed       # watch the browser
```

## Possible extensions

- Run across Chromium / Firefox / WebKit (`--browser firefox`)
- Add screenshots/traces on failure (`--tracing retain-on-failure`)
- Parallel runs with `pytest-xdist`
