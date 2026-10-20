"""
Overdraft service charge strategy module.
Defines the overdraft service charge calculation strategy
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """ Service charge strategy for overdraft accounts."""


    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """ Initialize the overdraft service charge strategy with
            overdraft limit and overdraft rate.
        Args:
            overdraft_limit (float): The overdraft limit for the account.
            overdraft_rate (float): The overdraft rate for the account.
        """
        self.__overdraft_limit = float(overdraft_limit)
        self.__overdraft_rate = float(overdraft_rate)

    def calculate_service_charges(self, account: BankAccount) -> float:
        """ Calculate and return the service charge for the given overdraft 
        account.

        Args:
            account (BankAccount): The bank account for which to calculate
            the service charge.
            Returns:
        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE

        overdraft = self.__overdraft_limit - account.balance
        
        return self.BASE_SERVICE_CHARGE + (overdraft) * self.__overdraft_rate