"""
Minimum balance strategy module.    
Defines the minimum balance requirement strategy for bank accounts.
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """ Service charge strategy for accounts based on
        minimum balance requirement.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(self, minimum_balance: float):
        """ Initialize the minimum balance strategy with minimum balance.
        Args:
            minimum_balance (float): The minimum balance requirement for 
            the account.
        """
        self.__minimum_balance = float(minimum_balance)

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Returns the service charges based on minimum balance strategy.
        """
        if account.balance <= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
    
        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM