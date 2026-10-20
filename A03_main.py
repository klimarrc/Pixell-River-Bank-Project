"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from datetime import date
from bank_account import *
from client.client import Client

# 2. Create a Client object with data of your choice.
client1 = Client(
    client_number=1,
    last_name="Doe",
    first_name="John",
    email_address="john.doe@example.com"
)

# 3a. Create a ChequingAccount object with data of your choice, using the client_number
# of the client created in step 2.
chequing_account1 = ChequingAccount(
    account_number=1001,
    client_number=client1.client_number,
    balance=500.0,
    date_created=date(2020, 1, 1),
    overdraft_limit=-100.0,
    overdraft_rate=0.05
)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number
# of the client created in step 2.
savings_account1 = SavingsAccount(
    account_number=1002,
    client_number=client1.client_number,
    balance=1000.0,
    date_created=date(2020, 1, 1),
    minimum_balance=100.0
)




# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object. 
 
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account1.attach(client1)
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account1.attach(client1)

# 5a. Create a second Client object with data of your choice.
client2 = Client(
    client_number=2,
    last_name="Johnson",
    first_name="Emily",
    email_address="emily.johnson@example.com"
)

# 5b. Create a SavingsAccount object with data of your choice, using the client_number
# of the client created in this step.
savings_account2 = SavingsAccount(
    account_number=1005,
    client_number=client2.client_number,
    balance=1500.0,
    date_created=date(2022, 6, 1),
    minimum_balance=100.0
)




# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# chequing_account1 transactions
try:
    chequing_account1.withdraw(5.00)  # Should trigger low balance notification
except Exception as e:
    print(f"Error: {e}")
try:
    chequing_account1.withdraw(2000.75)  # Should not trigger any notification
except Exception as e:
    print(f"Error: {e}")
try:
    chequing_account1.deposit(10.50)  # Should trigger large transaction notification  
except Exception as e:
    print(f"Error: {e}")        

# savings_account1 transactions
try:
    savings_account1.withdraw(950.0)  # Should trigger low balance notification  
except Exception as e:
    print(f"Error: {e}")
try:    
    savings_account1.withdraw(50.0)  # Should not trigger any notification   
except Exception as e:
    print(f"Error: {e}") 
try:            
    savings_account1.deposit(15000.0)  # Should trigger large transaction notification       
except Exception as e:
    print(f"Error: {e}")    

# savings_account2 transactions
try:
    savings_account2.withdraw(1400.0)  # Should trigger low balance notification    
except Exception as e:
    print(f"Error: {e}")    
try:    
    savings_account2.withdraw(50.0)  # Should not trigger any notification                  
except Exception as e:
    print(f"Error: {e}")
try:        
    savings_account2.deposit(20000.0)  # Should trigger large transaction notification
except Exception as e:
    print(f"Error: {e}")  
