""" Test investment account features
"""
import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    """ Unit tests for the InvestmentAccount class.
    """
   
    # Base service charge for testing
    

    def setUp(self):
        """ Set up test variables.
        """
        self.investment = InvestmentAccount(
            account_number=1000,
            client_number=1,
            balance=100.0,
            date_created=date.today() - timedelta(days=10 * 365),
            management_fee=2.5)

    def test_set_attributes_paramenters(self):
        """ Test initialization of InvestmentAccount.
        """
        self.assertEqual(1000, self.investment.account_number)
        self.assertEqual(1, self.investment.client_number)
        self.assertEqual(100.0, self.investment.balance)
        self.assertEqual(date.today() - timedelta(days=10 * 365), 
                         self.investment.date_created)
        self.assertEqual(2.5, self.investment._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_sets_default(self):
        """ Test creating an investment account with invalid management fee.
        """
        #Arrange

        #Act
        investment = InvestmentAccount(1001, 2, 200.0, date.today(), "two")

        #Assert
        self.assertEqual(2.55,investment._InvestmentAccount__management_fee)

   
    def test_get_service_charge_date_created_more_than_ten_years(self):
        """ Test get_service_charge method for account older than 10 years.
        """
        #Arrange
        investment = InvestmentAccount(account_number=1000,
                                       client_number=1,
                                       balance=100.0,
                                       date_created=date(2010, 10, 1),
                                       management_fee=2.5)
        #Act
        BASE_SERVICE_CHARGE = 0.50
        excepted = BASE_SERVICE_CHARGE
        actual = investment.get_service_charges()
        #Assert
        self.assertEqual(excepted, round(actual, 2))

    def test_get_service_charge_date_created_exactly_ten_years(self):
        """ Test get_service_charge method for account exactly 10 years old.
        """
        #Arrange
        BASE_SERVICE_CHARGE = 0.50
        #Act
        excepted = BASE_SERVICE_CHARGE + 2.5
        actual = self.investment.get_service_charges()
        #Assert
        self.assertEqual(excepted, round(actual, 2))
    
    def test_str_date_created_more_than_ten_years(self):
        """ Test get_service_charge method for account more than 10 years old.
        """
        #Arrange
        
        investment = InvestmentAccount(account_number=1000,
                                       client_number=1,
                                       balance=100.0,
                                       date_created=date(2010, 10, 1),
                                       management_fee=2.5)
        #Act
        actual = str(investment)
        #Assert
        self.assertIn("Management Fee: $2.50".lower(), actual.lower())

    def test_get_service_charge_date_created_less_than_ten_years(self):
        """ Test get_service_charge method for account less than 10 years old.
        """
        #Arrange
        investment = InvestmentAccount(account_number=1000,
                                       client_number=1,
                                       balance=100.0,
                                       date_created=date(2020, 10, 1),
                                       management_fee=2.5)
        #Act
        actual = str(investment)
        #Assert
        self.assertIn("Management Fee: Waived".lower(), actual.lower())

    def test_str_date_created_within_ten_years(self):
        """ Test __str__ method for account exactly 10 years old.
        """
        #Arrange
        investment = InvestmentAccount(account_number=1000,
                                       client_number=1,
                                       balance=100.0,
                                       date_created=date(2010, 1, 1),
                                       management_fee=2.5)
        #Act
        actual = str(investment)
        #Assert
        self.assertIn("Management Fee: $2.50", actual)
