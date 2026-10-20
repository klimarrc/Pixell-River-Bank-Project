""" Savings Account class module for bank account management system."""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """ A class to represent savings account is meant for a client
      with a long-term savings.
    """

    def __init__(self, account_number: int,
                client_number: int,
                balance: float,
                date_created: date,
                minimum_balance: float):
        """
        Initialize the savings account with minimum balance.

        Args:
            minimum_balance (float): The minimum balance for
            the savings account.
        """
        super().__init__(account_number, client_number,
                          balance, date_created)

        try:
            self._minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self._minimum_balance = 50.0

        self.__strategy = MinimumBalanceStrategy(self._minimum_balance)

    def get_service_charges(self) -> float:
        """
        Calculate service charges for the savings account.
        """
        return self.__strategy.calculate_service_charges(self)
        
    
    def __str__(self) -> str:
        """ Return a string representation of the savings account.

        Returns:
            str: A string containing the account number, balance, 
            and minimum balance.
        """
        return (f"{super().__str__()}\n"
                f"Minimum Balance: ${self._minimum_balance:.2f} "
                f"Account Type: Savings")
