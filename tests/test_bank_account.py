"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """ Unit tests for the BankAccount class.
    """

    def setUp(self):
        """ Set up test fixtures, if any. This method is called before
        each test function.
        """
        self.account = BankAccount(1000, 1, 100.0)

    def test_init_account_with_valid_attributes_account_set(self):
        """ Test creating a bank account with valid attributes.
        """
        #Arrange
        #Act
        #Assert
        self.assertEqual(1000, self.account.account_number)
        self.assertEqual(1, self.account.client_number)
        self.assertEqual(100.0, self.account.balance)

    def test_init_attributes_set_to_zero_with_non_numeric_balance(self):
        """ Test creating a bank account with non-float balance.
        """
        account = BankAccount(1000, 1, "zero")
        self.assertEqual(0.0, account.balance)

    def test_init_non_integer__account_number_raises_valueerror(self):
        """ Test creating a bank account with non-numeric account number.
        """
        #Arrange
        #Act
        #Assert
        with self.assertRaises(ValueError):
            BankAccount("one thousand", 1, 100)

    def test_init_non_integer_client_number_raises_valueerror(self):
        """ Test creating a bank account with invalid client number.
        """
        #Arrange
        #Act
        #Assert
        with self.assertRaises(ValueError):
            BankAccount(1000, "one", 100)

    def test_account_number_accessor_returns_account_number(self):
        """ Test the account number accessor method.
        """
        #Arrange
       

        #Act
        account_number = self.account.account_number

        #Assert
        self.assertEqual(1000, account_number)

    def test_client_number_accessor_returns_client_number(self):
        """ Test the client number accessor method.
        """
        #Arrange
       
        #Act
        client_number = self.account.client_number

        #Assert
        self.assertEqual(1, client_number)

    def test_balance_accessor_returns_current_balance(self):
        """ Test the balance accessor method.
        """
        #Arrange
       
        #Act
        balance = self.account.balance

        #Assert
        self.assertEqual(100, balance)
        
    def test_update_adds_positive_amount_balance_updated(self):
        """ Test updating the balance by adding a positive amount.
        """
        
        #Act
        self.account.update_balance(50)

        #Assert
        self.assertEqual(150, round(self.account.balance, 2))

    def test_update_negative_amount_balance_updated(self):
        """ Test updating the balance by subtracting a negative amount.
        """
        
        #Act
        self.account.update_balance(-20)

        #Assert
        self.assertEqual(80, round(self.account.balance, 2))

    def test_update_balance_unchanged_amount_non_numeric(self):
        """ Test updating the balance with a non-numeric amount.
        """
        # Arrange
        old_balance = self.account.balance
        #Act
        #Assert
        self.account.update_balance("fifty")
        self.assertEqual(old_balance, self.account.balance)

    def test_deposit_validamount_balance_updated(self):
        """ Test depositing a valid amount into the account.
        """
        #Arrange
        #Act
        self.account.deposit(25.0)

        #Assert
        self.assertEqual(125.0, round(self.account.balance, 2))

    def test_deposit_negative_amount_raises_valueerror(self):
        """ Test depositing a negative amount into the account.
        """
        #Arrange
        # Act
        #Assert
        with self.assertRaises(ValueError):
            self.account.deposit(-25)
        self.assertEqual(100.0, round(self.account.balance, 2))
    
    def test_withdraw_valid_amount_balance_updated(self):
        """ Test withdrawing a valid amount from the account.
        """
        #Arrange
        #Act
        self.account.withdraw(40.0)
        
        #Assert
        self.assertEqual(60.0, round(self.account.balance, 2))

    def test_withdraw_negative_amount_raises_valueerror(self):
        """ Test withdrawing a negative amount from the account.
        """
        #Act
        #Assert
        with self.assertRaises(ValueError):
            self.account.withdraw(-40)
        self.assertEqual(100.0, round(self.account.balance, 2))

    def test_withdraw_exceeding_balance_raises_valueerror(self):
        """ Test withdrawing an amount that exceeds the current balance.
        """
        #Act
        #Assert
        with self.assertRaises(ValueError):
            self.account.withdraw(5000)
        self.assertEqual(100.0, round(self.account.balance, 2))

    def __str__(self):
        """ Return the string representation of the bank account.
        """
        return "Account Number: {account_number},\nBalance: ${balance:.2f}"


