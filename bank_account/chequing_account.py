""" Chequing Account module for bank account management system."""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

__author__ = "Kailine Lima"
__version__ = "1.0.0"


class ChequingAccount(BankAccount):
    """ A class to represent a chequing account, inheriting from
    BankAccount.
        
    Implements overdraft limit and overdraft rate features.
    """
    DEFAULT_OVERDRAFT_LIMIT = -100.0
    DEFAULT_OVERDRAFT_RATE = 0.05
   
    def __init__(self, 
                account_number: int,
                client_number: int,
                balance: float,
                date_created: date,
                overdraft_limit: float,
                overdraft_rate: float
        ):
        """ Initialize the chequing account with overdraft limit and rate.
        Args:
            overdraft_limit (float): The overdraft limit for the 
            chequing account.
            overdraft_rate (float): The overdraft interest rate for
            the chequing account.
            strategy (OverdraftStrategy): The strategy for calculating
            service charges.
            """
        super().__init__(account_number, client_number, balance, date_created)
        
        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            try:
                self.__overdraft_limit = float(overdraft_limit)
            except (TypeError, ValueError):
                self.__overdraft_limit = self.DEFAULT_OVERDRAFT_LIMIT
        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            try:
                self.__overdraft_rate = float(overdraft_rate)
            except (TypeError, ValueError):
                self.__overdraft_rate = self.DEFAULT_OVERDRAFT_RATE

        self.__strategy = OverdraftStrategy(
                self.__overdraft_limit,
                self.__overdraft_rate
                )

    def get_service_charges(self) -> float:
        """
        Calculate service charges for the account.
        """


        return self.__strategy.calculate_service_charges(self)

    
    def __str__(self) -> str:
        """ Return a string representation of the chequing account.

        Returns:
            str: A string containing the account number, balance,
            overdraft limit, and overdraft rate.

        Format:
        Account Number: 123456 Balance: $500.00
        Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account 
        Type: Chequing
        """
        first_line = super().__str__()
        
        return (
            f"{first_line}\n"
            f"Overdraft Limit: ${self.__overdraft_limit:.2f} "
            f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
            f"Account Type: Chequing"
        )
    