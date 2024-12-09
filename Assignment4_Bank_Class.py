import random
class bank:

    def __init__(Favouredchi):
        Favouredchi.accounts = {}
        Favouredchi.total_bank_balance = 0.0

    def generate_account_number(Favouredchi):
        """Generates a unique 10-digit account number."""
        while True:
            account_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            if account_number not in Favouredchi.accounts:
                return account_number

    def create_number(self, account_holder, account_type, initial_deposit):
        """
        Creates a new bank account.
        Args: 
            account_holder (str): Name of account holder.
            account_type (str): Type of account (e.g., "Savings"),
            initial_deposit (float): Initial deposit amount.
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negetive")
        
        account_number = self.generate_account_number()
        self.accounts[account_number] = {
            "account_holder": account_holder,
            "account_type": account_type,
            "balance": initial_deposit
        }
        self.total_bank_balance += initial_deposit
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number
    
    def find_account(self, account_number):
        """
        Retrives an account by its account number.
        Args:
        account_number(str): The account number to search for.
        """
        return self.accounts.get(account_number, None)
    
    def delete_account(self, account_number):
        """
        Removes an account from the bank.
        Args:
            account_nymber (str): The account number to delete.
        """
        account = self.accounts.pop(account_number, None)
        if account:
            self.total_bank_balance -= account["balance"]
            print(f"Account {account_number} deleted successfully.")
        else:
            print(f"Account {account_number} not found.")
    
    def list_Accounts(Favouredchi):
        """Displays all accounts in the bank."""
        if not Favouredchi.accounts:
            print("No accounts in the bank")
            return
        print("Accounts in the bank")
        for acc_num, details in Favouredchi.accounts.items():
            print(f"Account Number: {acc_num}, Holder: {details['account_holder']}, Type: {details['account_type']}, Balance: {details['balance']}")
