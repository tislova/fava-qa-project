# Fava QA Testing Project

This project demonstrates both manual and automated testing for [Fava](https://beancount.github.io/fava/), a web interface for financial accounting using Beancount files.

The goal is to validate key logic and user interface components through manual test cases and automated testing using Pytest and Selenium.


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


## Features Tested

- **Journal View** – Verified transaction display and infinite scroll.
- **Filtering** – Tested filtering by payee, tag, and invalid inputs.
- **Accounts View** – Checked account hierarchy and balance rendering.
- **Reports** – Validated Balance Sheet and Income Statement views.
- **Editor** – Confirmed editing and saving of `.beancount` files.
- **Responsiveness** – Verified layout on desktop, tablet, and mobile.
- **Accessibility** – Reviewed basic keyboard and visual accessibility.

Manual tests were performed across **Chrome**, **Safari**, **Firefox**, and **Edge**.


## Technologies Used

- **Python 3.10+**  
- **Pytest** 
- **Selenium** - Chromedriver
- **Git & GitHub**  


## Running Tests

```bash
pip install pytest selenium
pytest tests/test_cases.py --driver Chrome
```


## Bug Reports

The following issues were identified during testing:

- **TC-06** – Raw HTML and JSON are shown when special characters are entered in the filter.  
- **TC-07** – Long descriptions in Journal View force horizontal scrolling instead of wrapping.  
- **TC-10** – Editor allows saving an empty transaction without validation.  
- **TC-18** – Future-dated transactions in Accounts View aren’t visually distinguished.  
- **TC-27** – Unbalanced transactions are saved but only show errors post-submission.  
- **TC-29** – Tag filters are case-sensitive when they should be case-insensitive.  
- **TC-32** – Metadata toggle in Journal View does not collapse metadata as expected.  
- **TC-33** – Keyboard tab navigation skips most focusable elements.  
- **TC-34** – Mobile layout still causes horizontal scrolling on smaller screens.

All bugs are documented with reproduction steps in:  
`manual-testing/test_cases.xlsx`