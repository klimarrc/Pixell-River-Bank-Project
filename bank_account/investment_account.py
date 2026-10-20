""" Investment Account class module for bank account management system."""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """ A class to represent an investment account is meant for a client
      with a long-term savings.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365)

    def __init__(self, account_number: int,
                client_number: int,
                balance: float,
                date_created: date,
                management_fee: float
                ):
        
        """ Initialize the investment account with management fee.
        Args:
            management_fee (float): The management fee for the investment 
            account.

        Raises:
            ValueError: If management fee is not a float or is negative.
        """
        super().__init__(account_number,
                        client_number,
                        balance,
                        date_created)
        
        if isinstance(management_fee, float):
            self.__management_fee = management_fee
        else:
            try:
                self.__management_fee = float(management_fee)
            except (TypeError, ValueError):
                self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(self.date_created,
                                                self.__management_fee)

    def get_service_charges(self) -> float:
        """
        Calculate service charges for the investment account.
        """
        return self.__strategy.calculate_service_charges(self)
    
    def __str__(self) -> str:

        """Method to return a string representation to ensure 
        that super class __str_ is utilized to produce results.
        """
        super_string = super().__str__()
        
        if self.date_created > self.TEN_YEARS_AGO:
            fee_string = "Management Fee: waived"
        else:
            fee_string = f"Management Fee: ${self.__management_fee:.2f}"
        
        return(f"{super_string}\n {fee_string} Account Type: Investment")
