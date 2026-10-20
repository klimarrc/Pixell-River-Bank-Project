""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.

    # try:
    my_client = Client(1, "Lima", "Kailine", "kailine.lima@example.com")
    print(my_client)
    # except ValueError as e:
    #     print(e)

 # 2. Declare a BankAccount object with an initial value of None.
    bank_account_1: BankAccount = None
 

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance.
    
    try:
        num = my_client.client_number
        bank_account_1 = BankAccount(1000, num, 100.0)
        print(bank_account_1)
    except ValueError as e:
        print(e)
    

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 

    try:
        bank_account_2 = BankAccount(1000, my_client.client_number, "one hundred")
    except ValueError as e:
        print(e)


    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(my_client)
    print(bank_account_1)




    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        bank_account_1.deposit("one hundred")
    except ValueError as e:
        print(e)



    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        bank_account_1.deposit(-50.0) 
    except ValueError as e:
        print(e)        


    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    try:
        bank_account_1.withdraw(50.0)
        print(f"New balance after withdrawal: {bank_account_1.balance}")
    except ValueError as e:
        print(e)


    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        bank_account_1.withdraw("fifty")      
    except ValueError as e:
        print(e)


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        bank_account_1.withdraw(-30.0)
    except ValueError as e:
        print(e)


    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        bank_account_1.withdraw(100.0)
    except ValueError as e:
        print(e)
 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(bank_account_1)

  
if __name__ == "__main__":
    main()