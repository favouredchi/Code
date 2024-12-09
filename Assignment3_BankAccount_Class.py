class BankAccount:
    def __init__(self, account_number, account_holder, account_type, balance=0):
        """
        Initialize the account with account number, account holder name, account type, and optional starting balance.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance
        self.transaction_log = []

    def deposit(self, amount):
        """
        Add money to the account.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_log.append(f"Deposited: ${amount:.2f}")
        print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Remove money from the account.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
            return
        self.balance -= amount
        self.transaction_log.append(f"Withdrew: ${amount:.2f}")
        print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """
        Return the current account balance.
        """
        print(f"Account balance: ${self.balance:.2f}")
        return self.balance

    def transfer(self, amount, target_account):
        """
        Transfer money from this account to a target account.
        """
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for this transfer.")
            return
        self.balance -= amount
        target_account.balance += amount
        self.transaction_log.append(f"Transferred: ${amount:.2f} to {target_account.account_holder} (Account: {target_account.account_number})")
        target_account.transaction_log.append(f"Received: ${amount:.2f} from {self.account_holder} (Account: {self.account_number})")
        print(f"Successfully transferred ${amount:.2f} to {target_account.account_holder}. New balance: ${self.balance:.2f}")

    def view_transaction_log(self):
        """
        Display the transaction log.
        """
        print("Transaction Log:")
        for transaction in self.transaction_log:
            print(transaction)
