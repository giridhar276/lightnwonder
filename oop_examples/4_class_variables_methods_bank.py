'''
You want to change the value of the class variable school_name.

This change should reflect across all existing and future instances of the class.

A @classmethod operates on the class itself, not on any individual instance.

It takes cls (the class) as its first argument instead of self (the instance).

Use @classmethod when you want to change or access class variables — variables that are shared by all instances.

Without @classmethod, you'd be modifying the variable for only one instance, not the whole class.

 What is cls?
cls is just a name, not a keyword in Python.

It refers to the class itself (like self refers to the instance).

It's not fixed — you could technically call it anything, but cls is the widely accepted convention.


'''

# Real-world example: Bank and Accounts

class Bank:
    bank_name = "National Trust Bank"  # Class variable shared across all accounts

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable

    @classmethod
    def change_bank_name(cls, new_name):
        """Change the name of the bank"""
        cls.bank_name = new_name

    def show_account_info(self):
        """Display account holder and bank information"""
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Create account holders
account1 = Bank("Alice")
account2 = Bank("Bob")

# Show initial bank information
account1.show_account_info()
account2.show_account_info()

# Change the bank name
Bank.change_bank_name("Global Finance Bank")

# Show updated bank information
account1.show_account_info()
account2.show_account_info()
