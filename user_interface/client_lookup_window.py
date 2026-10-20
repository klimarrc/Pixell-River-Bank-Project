__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):
    """A class used generate UI to look up clients and display their
    bank accounts."""
     
    def __init__(self):
        """
        Initializes the Client Lookup window by loading client
        and account data.
        """
        super().__init__()
        # Load client and account data
        self.client_listing, self.accounts = load_data()

        # Connect the lookup button to the lookup_client method
        self.lookup_button.clicked.connect(self.__on_lookup_client)

        # Connect the text changed signal to enable/disable the lookup button
        self.client_number_edit.textChanged.connect(self.__on_text_changed)

        # Connect the account table cell click signal to open account details
        self.account_table.cellClicked.connect(self.__on_account_selected)

        # Connect the filter button to the filter method
        self.filter_button.clicked.connect(self.__on_filter_clicked)
    
    
    def __on_lookup_client(self) -> None:
        """
        Slot for the lookup_button clicked signal.
        Looks up the client number entered and displays client and account info.
        """

        # The on_lookup_client method will act as a slot for 
        # the lookup_button clicked signal
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.information(self, "Non-Numeric Client",
                                    "The client number must be" \
                                    " an integer value.")
            self.reset_display()
            return
        
        #client = self.client_listing.get(client_number)
        if client_number not in self.client_listing:
            QMessageBox.information(self, "Client Not Found", 
            f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        # Display client information
        client = self.client_listing[client_number]
        client_name = f"Client Name: {client.first_name} {client.last_name}\n"
        self.client_info_label.setText(client_name)

        self.account_table.setRowCount(len(self.accounts))
        row = 0 

        for account in self.accounts.values():
            if account.client_number == client_number:
                # Create  QTableWidgetItem objects for account details
                # Account Number (string)
                account_number_item = QTableWidgetItem(str(account.account_number))
                account_number_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

                # Balance (current balance formatted to 2 decimal places)
                balance_item = QTableWidgetItem(f"${account.balance:.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                # Date Created (formatted as YYYY-MM-DD)
                date_created_item = QTableWidgetItem(account.date_created.strftime("%Y-%m-%d"))
                date_created_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter) 

                # Account Type (the class name of the BankAccount subclass)
                account_type_item = QTableWidgetItem(account.__class__.__name__)
                account_type_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  
                
                # Insert the items into the table
               
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)
                row += 1
    
        
        self.account_table.resizeColumnsToContents()

        self.__toggle_filter(False)


            
   
    def __on_text_changed(self) -> None:
        """
        Slot for the client_number_edit textChanged signal.
        Enables or disables the lookup button based on the input.
        """
       
        self.account_table.setRowCount(0)
      
       

    @Slot(int, int)
    def __on_account_selected(self, row: int, column: int) -> None:
        """ Slot for account_table cellClicked signal.
        Opens the AccountDetailsWindow for the selected account.
        Args:
            row (int): The row index of the clicked cell.
            column (int): The column index of the clicked cell.
        """
        # Get the account number item from the first column of the clicked row
        account_number_item = self.account_table.item(row, 0)
        
        if account_number_item is None or not account_number_item.text().strip():
            QMessageBox.information(self, "Invalid Selection", 
                                    "Please select a valid record.")
            return

        account_number_text = account_number_item.text().strip()

        try:
            account_number = int(account_number_text)
        except ValueError:
            QMessageBox.information(self, "Invalid Selection",
                                     "Account number is not a valid integer.")
            return

        if account_number not in self.accounts:
            QMessageBox.information(self, "Invalid Selection",
                                     "Bank account selected does not exist.")
            return

       
        account_number = int(account_number_text)  
        account = AccountDetailsWindow(self.accounts[account_number])

        # Connect the account_updated signal to the update_data function
        account.balance_updated.connect(self.__update_data)

        account.exec_()
    
    @Slot(BankAccount)
    def __update_data(self, account: BankAccount) -> None:
        """
        Slot to handle updating account data when notified.
        Args:
            account (BankAccount): The updated bank account object.
        """
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)
            if item and int(item.text()) == account.account_number:
                # Update the balance in the table
                balance_item = self.account_table.item(row, 1)
                balance_item.setText(f"${account.balance:,.2f}")
                self.accounts[account.account_number] = account
                break

    @Slot()   
    def __on_filter_clicked(self) -> None:
        """
        Slot for filter_button.clicked.

        Applies or clears a filter on account_table based on the current text
        of filter_button ("Apply Filter" vs anything else).
        """
        if self.filter_button.text() == "Apply Filter":
            # apply filter
            column_index = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text().lower()

            row_count = self.account_table.rowCount()

            for row in range(row_count):
                item = self.account_table.item(row, column_index)

                if item and search_text in item.text().lower():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

            # tell UI we are now filtered
            self.__toggle_filter(True)

        else:
            # tell UI we are now unfiltered
            self.__toggle_filter(False)
    
    @Slot(bool)
    def __toggle_filter(self, filter_on: bool) -> None:
        """
        Updates the filter button text based on the filter state.
        Args:
            is_filtered (bool): True if a filter is applied, False otherwise.
        """
        self.filter_button.setEnabled(True)

        if filter_on:

            # Button text
            self.filter_button.setText("Reset")

            # Disable the criteria widgets
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)

            # Label text
            self.filter_label.setText("Data is Currently Filtered")

        else:
            # Button text
            self.filter_button.setText("Apply Filter")

            # Enable criteria widgets
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)

            # Clear input and reset combo box
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            # Show all rows in the table again
            row_count = self.account_table.rowCount()
            for row in range(row_count):
                self.account_table.setRowHidden(row, False)

            # Label text
            self.filter_label.setText("Data is Not Currently Filtered")