# Test Plan: QA Automation Suite

## 1. Objective
Verify the core user flows of the SauceDemo web app (login, cart, checkout) and the JSONPlaceholder REST API, using an automated regression suite that runs locally and in CI.

## 2. Scope
**In scope**
- UI: login (valid, locked-out, invalid input), product listing, sorting, add/remove cart, checkout with validation
- API: GET, filtered GET, POST, PUT, DELETE, 404 handling, response time

**Out of scope**
- Performance/load testing, security testing, accessibility, mobile browsers
- Non-standard SauceDemo users (problem_user, performance_glitch_user, visual_user)

## 3. Test approach
| Type | How |
|------|-----|
| Smoke | `pytest -m smoke`, quick check that the critical paths work |
| Regression (automated) | Full `pytest` run on every push via GitHub Actions |
| Exploratory (manual) | Time-boxed sessions on login and checkout, see `test-cases.md` section B |
| API | `requests` against JSONPlaceholder, checking status, body and timing |

## 4. Tools
Python 3.12, pytest, Playwright (Chromium), requests, pytest-html, GitHub Actions, Git.

## 5. Environment
- UI: https://www.saucedemo.com (public demo site)
- API: https://jsonplaceholder.typicode.com (fake REST API; writes are simulated and not persisted)
- Browser: Chromium (Firefox/WebKit can be added with `--browser`)

## 6. Entry / exit criteria
- **Entry:** dependencies installed, target sites reachable
- **Exit:** all smoke tests pass, no open Critical/High defects, full suite green in CI

## 7. Risks
| Risk | Mitigation |
|------|------------|
| Public sites can be slow or down | Timeouts on API calls, rerun the CI job |
| Timing-related flaky UI tests | Wait on page state (selectors / `expect`), never fixed sleeps (see BUG-001) |
| Demo data can change | Keep assertions on stable behaviour, review failures before editing tests |

## 8. Reporting
HTML report at `reports/report.html`, uploaded as a CI artifact. Defects are logged using the template in `docs/bug-reports/`.
