"""Description: Bank Account module for managing bank account operations.
The Bank Account has an observer who must be notified of any change to the subject.

"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"



from abc import ABC, abstractmethod
from ast import List
from datetime import date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer


class BankAccount(Subject, ABC):
    """Abstract base class representing a bank account.

    Inheritance:
        - Subject: Enables observer registration and notifications.
        - ABC: Enforces abstract methods for subclass implementation.

    Subclasses (Chequing, Investment, Savings) inherit these observer capabilities.

    Constants:
        LOW_BALANCE_LEVEL (float): Threshold for low balance warnings.
        LARGE_TRANSACTION_THRESHOLD (float): Threshold for large transaction alerts.
    """
    LOW_BALANCE_LEVEL: float = 50.00
    LARGE_TRANSACTION_THRESHOLD: float = 10_000.00

    def __init__(self, 
                 account_number: int, 
                 client_number: int, 
                 balance: float, 
                 date_created: date):
        """Initialize the bank account with identifiers and an initial balance.

        Args:
            account_number (int): Unique identifier for the bank account.
            client_number (int): Unique identifier for the client who owns the account.
            balance (float): Initial balance of the bank account. Must be non-negative.
            date_created (date): The date the account was created.

        Raises:
            ValueError: If client_number is not an integer.
            ValueError: If the initial balance is negative.
        """


        
        Subject.__init__(self)
        self._observers: List[Observer] = []

       
        try:
            self.__account_number: int = int(account_number)
        except Exception:
            self.__account_number = 0

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer " \
            "number.")
        self.__client_number = client_number

        try:
            self.__balance: float = float(balance)
        except Exception:
            self.__balance = 0.0

         
        if isinstance(date_created, date):
            self.__date_created = date_created
        else: 
            self.__date_created = date.today()

        # ---- Observer (concrete implementations) ----
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for obs in list(self._observers):
            obs.update(message)

   
    def deposit(self, amount: float) -> None:
        """Deposit money into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount <= 0:
            raise ValueError(f"Amount:${amount:.2f} must be positive" 
                             "and greater than zero.")
        self.update_balance(+float(amount))

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative.
        """
        if amount <= 0:
            raise ValueError(f"Amount:${amount:.2f} "
                             "must be positive than zero.")
        if amount > self.balance:
            raise ValueError(f"Amount:${amount:.2f} "
                             f"must be less than ${self.balance:.2f}.")
        self.update_balance(-float(amount))

    def update_balance(self, amount: float) -> None:
        """Notifications:
            - Low balance warning if balance falls below LOW_BALANCE_LEVEL.
            - Large transaction alert if amount exceeds LARGE_TRANSACTION_THRESHOLD.

        Returns:
            None
        """


        
        self.__balance = float(self.__balance) + float(amount)

        
        if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
            self.notify(
                f"Low balance warning ${self.__balance:,.2f}: " 
                f"on account {self.__account_number}."
            )

        
        if abs(amount) > BankAccount.LARGE_TRANSACTION_THRESHOLD:
            self.notify(
                f"Large transaction ${abs(amount):,.2f}: "
                f"on account {self.__account_number}."
            )

    
    @property
    def account_number(self) -> int:
        """Returns the account number.

        :returns: The unique account identifier.
        :rtype: int
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """Returns the client number.
        
        :return: The unique client identifier.
        :rtype: int
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """Returns the current balance of the account
        :returns: The current account balance.
        :rtype: float
        """
        return self.__balance

    @property
    def date_created(self) -> date:
        """Returns the date the account was created.
        
        :returns: The account creation date.
        :rtype: date
        """
        return self.__date_created

    
    def __str__(self) -> str:
        """
        Return a string representation of the account.

        Returns:
            str: A readable summary of the account number and balance.
        """
        return f"Account Number: {self.__account_number} / " \
               f"Balance: ${self.__balance:,.2f}"

    @abstractmethod
    def get_service_charges(self) -> float:
        """Abstract method implemented by subclasses.

        Returns:
            float: The calculated service charges for the account.
        """
        pass
