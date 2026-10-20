"""
Service charge strategy pattern module.
Defines the interface for service charge calculation strategies.
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """ Abstract method representing the strategy for calculating
         service charges across different types of bank accounts."""
    
    BASE_SERVICE_CHARGE: float = 0.50


    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """ Calculate and return the service charge for the given bank 
        account.

        Args:
            account (BankAccount): The bank account for which to calculate
            the service charge.
        
        Returns:   
             float: The calculated service charge.
        """ 
        pass