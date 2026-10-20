"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

import unittest 
from email_validator import EmailNotValidError
from client.client import Client, DEFAULT_EMAIL 

class TestClient(unittest.TestCase):
    """ Unit tests for the Client class.
    """
    def setUp(self):
        """ Set up any state specific to the execution of the given class.
        """
        self.client = Client(1, "Lima", "Kailine", DEFAULT_EMAIL)
    
    def test_init_valid_client_attributes_client_set(self):
        """ Test creating a client with valid attributes.
       """
        client = Client(1, "Lima", "Kailine", DEFAULT_EMAIL)

        self.assertEqual(1, client.client_number)
        self.assertEqual("Lima", client.last_name)
        self.assertEqual("Kailine", client.first_name)
        self.assertEqual(client.email_address, DEFAULT_EMAIL)

    def test_init_invalid_client_number_raises_value_error(self):
        """ Test creating a client with invalid client number.
        """
        #Arrange
        #Act
        #Assert
        with self.assertRaises(ValueError):
            Client("one", "Lima", "Kailine", DEFAULT_EMAIL)

    def test_init_blank_last_name_raises_value_error(self):
        """ Test creating a client with blank first name.
        """
        #Arrange
        #Act
        #Assert
        with self.assertRaises(ValueError):
            Client(1, "   ", "Kailine", DEFAULT_EMAIL)
        
    def test_init_blank_first_name_raises_value_error(self):
        """ Test creating a client with blank last name.
        """
        #Arrange
        #Act
        #Assert
        with self.assertRaises(ValueError):
            Client(1, "Lima", "   ", DEFAULT_EMAIL)
        
    def test_init_invalid_email_address_sets_default_email(self):
        """ Test creating a client with invalid email address.
        """
        #Arrange
        #Act
        client = Client(1, "Lima", "Kailine", "invalid-email")

        #Assert
        self.assertEqual(client.email_address, DEFAULT_EMAIL)
        
    def test_client_number_accessor_valid_client_number_returned(self):
        """ Test the client number accessor.
        """
        #Arrange
        #Act
        #Assert
        self.assertEqual(1, self.client.client_number)

    def test_last_name_accessor_valid_last_name_returned(self):
        """ Test the last name accessor.
        """
        #Arrange
        #Act
        #Assert
        self.assertEqual("Lima", self.client.last_name)
    
    def test_first_name_accessor_valid_first_name_returned(self):
        """ Test the first name accessor.
        """
        #Arrange
        #Act
        #Assert
        self.assertEqual("Kailine", self.client.first_name)
    
    def test_email_address_accessor_valid_email_address_returned(self):
        """ Test the email address accessor.
        """
        #Arrange
        #Act
        #Assert
        self.assertEqual(self.client.email_address, DEFAULT_EMAIL)
