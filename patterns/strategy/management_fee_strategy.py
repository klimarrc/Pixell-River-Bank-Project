"""
Management fee strategy module.
Defines the management fee calculation strategy for investment accounts.
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"


from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """ Service charge strategy for investment accounts based on
        management fee.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365)

    def __init__(self, date_created: date, management_fee: float):
        """ Initialize the management fee strategy with management fee.
        Args:
            date_created (date): The date the account was created.
            management_fee (float): The management fee for the 
            investment account.
        """
        

        self.__management_fee = float(management_fee)
        self.__date_created = date_created

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculate service charges based on account creation date.
        The account parameter is unused for this strategy but kept for 
        interface compatibility.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + self.__management_fee
    
