def calculate_interest(principal, annual_rate, years, compounding_frequency=1):
    return principal * (1 + annual_rate / compounding_frequency) ** (compounding_frequency * years)

class Account:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self.balance = balance
        self.history = []

    def __repr__(self):
        return f"{self.account_type} Account - Balance: ${self.balance:.2f}"

users = {}

def register_user(username, password):
    if username in users:
        return "User already exists!"
    users[username] = {"password": password, "accounts": []}
    return "Registration successful!"

def authenticate_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

from datetime import datetime

def record_transaction(account, transaction_type, amount):
    transaction = {
        "timestamp": datetime.now(),
        "type": transaction_type,
        "amount": amount,
    }
    account.history.append(transaction)

def print_transaction_history(account):
    for tx in account.history:
        print(f"{tx['timestamp']}: {tx['type']} - ${tx['amount']:.2f}")

def enforce_minimum_balance(account, minimum_balance):
    if account.balance < minimum_balance:
        print("Minimum balance not maintained!")
        return False
    return True

def apply_fee(account):
    fee_structure = {
        "Checking": 5.0,
        "Savings": 2.0,
        "Business": 10.0
    }
    fee = fee_structure.get(account.account_type, 0)
    account.balance -= fee
    record_transaction(account, "Fee Deduction", fee)


