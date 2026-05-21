# Fava QA Testing Project

End-to-end quality assurance for [**Fava**](https://beancount.github.io/fava/), 
the web interface for [Beancount](https://beancount.github.io/) plain-text 
accounting. This project combines **manual test case design** with 
**automated browser testing** using Pytest and Selenium to validate Fava's 
core UI and business logic.

![Python](https://img.shields.io/badge/python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## Overview

Fava is a complex financial reporting tool with multiple interconnected views, 
file editing, filtering, and reporting features. This project tests it from a 
real user's perspective: can a user filter transactions correctly, edit a 
`.beancount` file safely, view balance sheets, and navigate the app on mobile?

**Approach:** I designed 34 manual test cases across 7 functional areas, 
executed them across 4 browsers, then automated a subset of regression-critical 
cases with Selenium. Bugs were documented with reproduction steps and 
severity classification.

## Key Findings — 9 Bugs Identified

During testing I identified and documented 9 reproducible bugs spanning UI, 
data integrity, accessibility, and security concerns.

**High severity:**
- **TC-06** — Raw HTML and JSON exposed when special characters entered in the filter (security/UI concern)
- **TC-10** — Editor saves empty transactions without validation (data integrity)
- **TC-27** — Unbalanced transactions save successfully; error appears only post-submission (data integrity)
- **TC-33** — Keyboard tab navigation skips most focusable elements (accessibility)

**Medium severity:**
- **TC-29** — Tag filters are case-sensitive when they should be case-insensitive
- **TC-34** — Mobile layout causes horizontal scrolling on smaller viewports

**Low severity:**
- **TC-32** — Metadata toggle in Journal View doesn't collapse as expected
- **TC-18** — Future-dated transactions not visually distinguished in Accounts View
- **TC-07** — Long descriptions force horizontal scroll instead of wrapping

Full reproduction steps and expected vs actual behavior documented in 
[`manual-testing/test_cases.xlsx`](manual-testing/test_cases.xlsx).

## Test Coverage

- **Journal View** — Transaction display, infinite scroll, metadata toggle
- **Filtering** — Payee, tag, and account filters, invalid input handling
- **Accounts View** — Hierarchy rendering, balance calculations, date highlighting
- **Reports** — Balance Sheet and Income Statement accuracy
- **Editor** — Saving valid and invalid `.beancount` files, validation logic
- **Responsive Design** — Layout integrity on desktop, tablet, and mobile viewports
- **Accessibility** — Keyboard navigation, focus indicators, visual contrast

**Cross-browser coverage:** Chrome, Safari, Firefox, Edge.

## Tech Stack

- **Python 3.10+** — Test logic and helpers
- **Pytest** — Test runner and assertion framework
- **Selenium WebDriver** — Browser automation with ChromeDriver
- **Excel / `xlsx`** — Manual test case documentation and tracking

## Project Structure

```plaintext
fava-qa-project/
├── fava/
│   ├── __init__.py
│   └── helpers.py
├── tests/
│   └── test_cases.py
├── manual-testing/
│   ├── test_cases.xlsx
│   └── data/
│       ├── example.beancount
│       └── journal.beancount
├── .gitignore
└── README.md
```

## Running the Tests

**Prerequisites:** Python 3.10+, Chrome browser, ChromeDriver matching your Chrome version, and a running Fava instance at `http://localhost:5000` for the Selenium tests.

```bash
#Install dependencies
pip install pytest selenium

#Download ChromeDriver
#https://chromedriver.chromium.org/downloads

#Run the full suite
pytest tests/test_cases.py
```

## Skills Demonstrated

- **Test case design** — Wrote 34 structured test cases with preconditions, steps, expected results, and actual results
- **Test automation** — Built Selenium + Pytest suite for regression-critical paths
- **Cross-browser testing** — Validated across Chrome, Safari, Firefox, Edge
- **Responsive testing** — Verified breakpoints across viewports
- **Accessibility evaluation** — Manual checks for keyboard navigation and focus management
- **Bug reporting** — Documented findings with severity, category, and reproduction steps
- **Open source QA workflow** — Tested an active open source project as an external contributor

## What I'd Add With More Time

- Open GitHub issues on the upstream Fava repository for confirmed bugs
- Expand automated coverage to include the Reports views
- Set up CI to run the automated suite on every commit (GitHub Actions)
- Add API-level testing for Fava's underlying endpoints

---

*Built as an independent QA project to practice professional software 
testing workflows. Fava and Beancount are open source projects by 
Martin Blais and Jakob Schnitzer. This project is not affiliated.*
