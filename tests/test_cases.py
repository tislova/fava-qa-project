from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fava.helpers import (text_filter,
    wrap_long_description,
    validate_transaction_date,
    duplicate_transaction,
    calculate_balance,
    parse_transaction_line,
)

def test_text_filter():
    data = [{"desc": "Restaurant"}, {"desc": "Starbucks"}]
    result = text_filter(data, "Starbucks")
    assert result == [{"desc": "Starbucks"}]

def test_text_filter_case_insensitive():
    data = [{"desc": "starbucks"}, {"desc": "Restaurant"}]
    result = text_filter(data, "Starbucks")
    assert result == [{"desc": "starbucks"}]

def test_text_filter_no_match():
    data = [{"desc": "Food"}, {"desc": "Restaurant"}]
    result = text_filter(data, "Starbucks")
    assert result == []

def test_wrap_long_description_1():
    assert wrap_long_description("Short") == "Short"

def test_wrap_long_description_2():
    assert wrap_long_description("This is a very long sentence") == "This is a very long ..."

def test_validate_transaction_date_invalid():
    assert validate_transaction_date("2023-08-01") is False

def test_validate_transaction_date_valid():
    assert validate_transaction_date("08/01/2023") is True

def test_validate_transaction_date_empty():
    assert validate_transaction_date("") is False

def test_duplicate_transaction_true():
    tx1 = {"desc": "Coffee", "amount": 5.0}
    tx2 = {"desc": "Coffee", "amount": 5.0}
    assert duplicate_transaction(tx1, tx2)

def test_duplicate_transaction_false():
    tx1 = {"desc": "Coffee", "amount": 5.0}
    tx2 = {"desc": "Food", "amount": 5.0}
    assert not duplicate_transaction(tx1, tx2)

def test_calculate_balance():
    transactions = [{"amount": 10}, {"amount": -2}, {"amount": 5}]
    assert calculate_balance(transactions) == 13

def test_calculate_balance_empty():
    assert calculate_balance([]) == 0

def test_parse_transaction_line():
    line = "01/01/2025,Groceries,100.50"
    result = parse_transaction_line(line)
    assert result == {"date": "01/01/2025", "desc": "Groceries", "amount": 100.5}

def test_parse_transaction_line_invalid():
    try:
        parse_transaction_line("value")
        assert False
    except IndexError:
        assert True

def test_parse_transaction_line_negative_amount():
    line = "01/01/2025,Refund,-50.00"
    result = parse_transaction_line(line)
    assert result == {"date": "01/01/2025", "desc": "Refund", "amount": -50.0}

def test_homepage_title():
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("http://localhost:5000") 
    assert " - Example Beancount file" in driver.title
    driver.quit()

def test_filter_box_visible():
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("http://localhost:5000")
    filter_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter by tag, payee, ..."]')
    assert filter_input.is_displayed()
    driver.quit()