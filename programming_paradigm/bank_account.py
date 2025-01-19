class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: float, default is 0
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        :param amount: float
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        :param amount: float
        :return: bool - True if successful, False otherwise
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdraw amount must be greater than zero.")
            return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
