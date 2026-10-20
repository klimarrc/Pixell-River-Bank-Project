""" Description: A class to handle client information with validation.
"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

DEFAULT_EMAIL = "email@pixell-river.com"

class Client(Observer):
    """ A class is designed to represent a client's information: 
    client_number first_name, last_name and email_address. It provide
    basic validation for each attribute.
    """
    def __init__(self, client_number: int, last_name: str, first_name: str, 
                 email_address: str):
        """Represents a client in the PiXELL River Financial System.

        :param client_number: Unique identifier for the client.
        :type client_number: int
        :param first_name: Client's first name.
        :type first_name: str
        :param last_name: Client's last name.
        :type last_name: str
        :param email_address: Client's email address.
        :type email_address: str
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")
        
        if first_name.strip():
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        
        if last_name.strip():
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        try:
            valid = validate_email(email_address, check_deliverability=False)
            self.__email_address = valid.email
        except EmailNotValidError:
            self.__email_address = DEFAULT_EMAIL 

    @property
    def client_number(self) -> int:
        """Returns the current value of the client_number attribute.

        :returns: The current value of the client_number attribute.
        :rtype: int
        """
        return self.__client_number
    
    @property
    def last_name(self) -> str:
        """Returns the last name.

        :returns: The current value of the last_name attribute.
        :rtype: str
        """
        return self.__last_name
    
    @property
    def first_name(self) -> str:
        """Returns the first name.

        :returns: The current value of the first_name attribute.
        :rtype: str
        """
        return self.__first_name
    
    @property
    def email_address(self) -> str:
        """Returns the current value of the email_address attribute.
        :returns: The current value of the email_address attribute.
        :rtype: str
        """
        return self.__email_address 
    
    def __str__(self) -> str:
        """ String representation of the client's information .
        Returns:
            str: Formatted string with client information.
        """
        return f"{self.__last_name}, {self.__first_name}, " \
               f"[{self.__client_number}] - {self.__email_address}\n"
    
    def update(self, message: str) -> None:
        """Called by Subject (BankAccount) when a notable event occurs.

        Subject format:
          ALERT: Unusual Activity: {current date/time}
        Message format:
          Notification for {client number}: 
          {first name} {last_name}: {message}
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        body = (
            f"Notification for {self.client_number}: "
            f"{self.first_name} {self.last_name}: {message}"
        )
        simulate_send_email(self.email_address, subject, body)

