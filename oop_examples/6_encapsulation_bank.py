


class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder   # Private variable
        self.__balance = balance                 # Private variable

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance! Cannot be negative.")

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    # Display account info
    def display(self):
        print(f"Account Holder: {self.__account_holder}, Balance: ${self.__balance}")

# Create a bank account
account = BankAccount("Alice", 500)

# Display initial info
account.display()

# Deposit some money
account.deposit(200)

# Withdraw some money
account.withdraw(100)

# Try to set invalid balance manually
account.balance = -300   # Should not allow

# Update balance manually (valid)
account.balance = 1000
account.display()
