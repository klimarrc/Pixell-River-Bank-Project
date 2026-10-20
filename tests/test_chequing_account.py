""" Test Chequing Account class is to ensure all methods work 
as expected.
"""
import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount  

__author__ = "Kailine Lima"
__version__ = "1.0.0"


class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class."""

    def setUp(self):
        """Create a ChequingAccount instance for testing."""

        self.initial_overdraft_limit = -100.0
        self.initial_overdraft_rate = 0.05

        self.chequing = ChequingAccount(
            account_number=1000,
            client_number=1,
            balance=100.0,
            date_created=date.today(),
            overdraft_limit=self.initial_overdraft_limit,
            overdraft_rate=self.initial_overdraft_rate
        )
        
    def test_init_set_attributes_with_input_values(self):
        """Test the initialization of the ChequingAccount."""

        self.assertEqual(self.chequing.account_number, 1000)
        self.assertEqual(self.chequing.client_number, 1)
        self.assertEqual(self.chequing.balance, 100.0)
        self.assertEqual(self.chequing.date_created, date.today())
    
    def test_get_service_charge_balance_greater_than_overdraft_limit(self):
        """Test calculating service charge when balance is within 
        overdraft limit.
        """
        
        #Arrange
        self.chequing.update_balance(-90.0)
        BASE_SERVICE_CHARGE = 0.50
        #Assert
        #Act
        excepted = BASE_SERVICE_CHARGE
        actual = self.chequing.get_service_charges()
        #Assert
        self.assertEqual(excepted, round(actual, 2))


    def test_get_service_charge_balance_less_than_overdraft_limit (self):
        """Test calculating service charge when balance exceeds 
        overdraft limit.
        """
        #Arrange    
        self.chequing.update_balance(-210.0)
        BASE_SERVICE_CHARGE = 0.50  
        #Act
        expected = BASE_SERVICE_CHARGE + \
                   (self.initial_overdraft_limit - self.chequing.balance) \
                   * self.initial_overdraft_rate
        actual = self.chequing.get_service_charges()
        #Assert
        self.assertEqual(expected, round(actual, 2))

    def test_get_service_charge_balance_equal_to_overdraft_limit (self):
        """Test calculating service charge when balance 
        equals overdraft limit."""

        #Arrange    
        self.chequing.update_balance(-200.0)
        BASE_SERVICE_CHARGE = 0.50  
        #Act
        expected = BASE_SERVICE_CHARGE
        actual = self.chequing.get_service_charges()
        #Assert
        self.assertEqual(expected, round(actual, 2))

    def test_str_correct_string_representation(self):
        """Test the string representation of the ChequingAccount."""
        
        # Arrange
        expected_str = ("Account Number: 1000 Balance: $100.00\n"
                        "Overdraft Limit: $-100.00 Overdraft Rate:"
                        " 5.00% Account Type: Chequing")
        
        # Act and Assert
        self.assertEqual(str(self.chequing), expected_str)