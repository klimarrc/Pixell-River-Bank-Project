__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
from user_interface.manage_data import update_data

from PySide6.QtCore import Slot
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account
    transactions.
    """
    # Signal emitted when the account balance is updated.
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        # If the account parameter is not of BankAccount type, 
        # close the Window using the reject() method.
        if not isinstance(account, BankAccount):
            self.reject()
            return
    
        # Store a copy of the account to avoid modifying 
        # the original directly
        self.account = copy.copy(account)

        
        # Display account information
        self.account_number_label.setText(f"{self.account.account_number}")
        
        # Display formatted balance
        self.balance_label.setText(f"${self.account.balance:,.2f}")

        # Connect deposit button to its slot
        self.deposit_button.clicked.connect(self.__on_apply_transaction)

        # Connect the withdraw button to its slot
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)

        # Connect the close button to exit the window
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self):
        """Slot for both deposit_button and withdraw_button.
        Validates amount, applies transaction, updates balance_label.
        Shows QMessageBox on failures as per rubric.
        """
        try:
            amount_text = self.transaction_amount_edit.text().strip()
            amount = float(amount_text)
        except Exception:
            QMessageBox.information(self, "Invalid Amount", 
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        # Determine which button sent the signal and 
        # apply the transaction
        transaction = " "
        try:
           # default label in case of unexpected sender
            sender = self.sender()

            if sender is self.deposit_button:
                transaction = "Deposit"
                self.account.deposit(amount)
            elif sender is self.withdraw_button:
                transaction = "Withdraw"
                self.account.withdraw(amount)
            else:
                transaction = "Unknown"
                # Unexpected source; treat as error so the user gets feedback
                raise RuntimeError("Unknown transaction source.")
                
            # Update the balance display
            self.balance_label.setText(f"${self.account.balance:,.2f}")
           
            # The transaction amount edit empty and focused
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(self, f"{transaction} failed", f"{str(e)}")

        # The transaction amount edit focused and empty
        self.transaction_amount_edit.setText("")
        self.transaction_amount_edit.setFocus()

        # Emit the balance_updated signal with the updated account
        self.balance_updated.emit(self.account)

        update_data(self.account)
                
        
    @Slot()
    def __on_exit(self):
 
        """Slot for the exit_button clicked signal.
           Exits the window with QDialog accept().
        """
        self.close()
         