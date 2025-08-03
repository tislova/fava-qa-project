def text_filter(data, keyword):
    return [item for item in data if keyword.lower() in item["desc"].lower()]

def wrap_long_description(text, max_len=20):
    return text if len(text) <= max_len else text[:max_len] + '...'

def validate_transaction_date(date_str):
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False
    
def duplicate_transaction(tx1, tx2):
    return tx1["desc"] == tx2["desc"] and tx1["amount"] == tx2["amount"]

def calculate_balance(transactions):
    return sum(t["amount"] for t in transactions)

def parse_transaction_line(line):
    parts = line.split(',')
    return {"date": parts[0], "desc": parts[1], "amount": float(parts[2])}