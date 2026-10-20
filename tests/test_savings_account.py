""" Test Savings Account class is to ensure all methods work 
as expected."""

__author__ = "Kailine Lima"
__version__ = "1.0.0"


import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class TestSavingsAccount(unittest.TestCase):
    """Unit tests for the SavingsAccount class."""

    def setUp(self):
        """Create a SavingsAccount instance for testing."""
        self.savings = SavingsAccount(
            account_number=1000,
            client_number=1,
            balance=1000.0,
            date_created=date.today(),
            minimum_balance=100.
        )

    def test_init_set_attributes_with_input_values(self):
        """Test the initialization of the SavingsAccount."""
        self.assertEqual(self.savings.account_number, 1000)
        self.assertEqual(self.savings.client_number, 1)
        self.assertEqual(self.savings.balance, 1000.0)
        self.assertEqual(self.savings.date_created, date.today())
        
        

    def test_get_service_charge_greater_than_minimum_balance(self):
        """Test calculating service charge when balance is below minimum balance."""
        self.savings.update_balance(-1000.0)
        expected = MinimumBalanceStrategy.BASE_SERVICE_CHARGE
        actual = self.savings.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_get_service_charge_equal_minimum_balance(self):
        """Test calculating service charge when balance is above minimum balance."""
        self.savings.update_balance(-900.0)
        expected = MinimumBalanceStrategy.BASE_SERVICE_CHARGE
        actual = self.savings.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_get_service_charge_above_minimum_balance(self):
        """Test calculating service charge when balance is above minimum balance."""
        self.savings.update_balance(100.0)
        expected = MinimumBalanceStrategy.BASE_SERVICE_CHARGE \
            * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM
        actual = self.savings.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_str_correct_string_representation(self):
        """Test the string representation of the SavingsAccount."""
        expected_str = ("Account Number: 1000 Balance: $1,000.00\n"
                        "Minimum Balance: $100.00 Account Type: Savings")
        self.assertEqual(expected_str, str(self.savings))
