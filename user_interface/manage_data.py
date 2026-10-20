__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"


import email
import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging

from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from client.client import Client




# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE

# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************

def load_data() -> tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple: (client_listing, accounts)
            - client_listing: { client_number: Client }
            - accounts:      { account_number: BankAccount subclass }
    """
    client_listing: dict[int, Client] = {}
    accounts: dict[int, BankAccount] = {}

    def _to_float_or_default(value: str | None, default: float = 0.0) -> float:
        s = (value or "").strip()
        if not s or s.lower() == "null":
            return default
        return float(s)

    # READ CLIENT DATA
    try:
        with open(clients_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                for record in reader:
                    client_number = int(record['client_number'].strip())
                    first_name = record['first_name'].strip()
                    last_name = record['last_name'].strip()
                    email_address = record['email_address']
                    
                    client = Client(
                        client_number = client_number,  
                        first_name = first_name, 
                        last_name = last_name,
                        email_address = email_address
                    )

                    client_listing[client.client_number] = client
                    
            except Exception as e:
                       
                        # root - ERROR - Unable to create client: First Name cannot be blank.
                logging.error(f"Unable to create client: {e}")

            logging.info(f"Successfully loaded {len(client_listing)} client records.")
    except FileNotFoundError as e:
        logging.error(f"Unable to open client file: {e}")
    except Exception as e:
        logging.error(f"Error reading clients.csv: {e}")

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                for record in reader:
                    account_number = int(record['account_number'].strip())
                    client_number = int(record['client_number'].strip())
                    balance = float(record['balance'])
                    date_created = datetime.strptime(record['date_created'],
                                                    '%Y-%m-%d').date()
                    account_type = record['account_type']
                    
                    
                   
                    
                    if account_type == "ChequingAccount":
                        overdraft_limit = float(record.get("overdraft_limit"))
                        overdraft_rate = float(record.get("overdraft_rate"))
                        account_obj = ChequingAccount(
                            account_number = account_number, 
                            client_number = client_number, 
                            balance = balance, 
                            date_created = date_created, 
                            overdraft_limit = overdraft_limit, 
                            overdraft_rate = overdraft_rate
                        )
                    elif account_type == "SavingsAccount":
                        minimum_balance = float(record.get("minimum_balance"))
                        account_obj = SavingsAccount(
                            account_number = account_number, 
                            client_number = client_number, 
                            balance = balance, 
                            date_created = date_created, 
                            minimum_balance = minimum_balance
                        )
                    elif account_type == "InvestmentAccount":
                        management_fee = float(record.get("management_fee"))
                        account_obj = InvestmentAccount(
                            account_number = account_number,
                            client_number = client_number, 
                            balance = balance, 
                            date_created = date_created,
                            management_fee = management_fee
                        )
                    else:
                        raise ValueError("Not a valid account type.")
                    
                    
                    if client_number in client_listing:
                        accounts[account_number] = account_obj
                    else:
                         logging.error(f"Unable to create bank account: Client number {client_number} not found for account {account_number}.")
                    
            except Exception as e:
                logging.error(f"Unable to create bank account: {e}")
            logging.info(f"Successfully loaded {len(accounts)} accounts.")
    except FileNotFoundError:
        logging.error(f"File not found: {accounts_csv_path}")
    except Exception as e:
        logging.error(f"Error reading accounts.csv: {e}")

    
    # RETURN STATEMENT
    return client_listing, accounts
    

def update_data( updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)
 
 
# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()
        
    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")