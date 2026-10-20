"""Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"



# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime


from datetime import date
from patterns import *
from bank_account import *



# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    account_number=1001,
    client_number=1,
    balance=50.0,
    date_created=date.today(),
    overdraft_limit=100.0,
    overdraft_rate=0.05  # Example value for overdraft_rate
)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print(chequing_account)
print(f"Service Charge: ${chequing_account.get_service_charges():.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.

chequing_account.update_balance(50.0)

# 4b. Print the ChequingAccount
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print(f"Service Charge: ${chequing_account.get_service_charges():.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

savings_account = SavingsAccount(
    account_number=2001,
    client_number=1,
    balance=500.0,
    date_created=date.today(),
    minimum_balance=100.0
)


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print(savings_account)
print(f"Service Charge: ${savings_account.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.update_balance(-450.0)

# 7b. Print the SavingsAccount.
print(savings_account)

# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.

print(f"Service Charge: ${savings_account.get_service_charges():.2f}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.

investment_account = InvestmentAccount(
    account_number=3001,
    client_number=1,
    balance=1000.0,
    date_created=date(2020, 1, 1),
    management_fee=20.0
)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.

print(investment_account)
print(f"Service Charge: ${investment_account.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(
    account_number=3002,
    client_number=1,
    balance=1000.0,
    date_created=date(2000, 1, 1),
    management_fee=25.0
)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.

print(investment_account_old)
print(f"Service Charge: ${investment_account_old.
                          get_service_charges():.2f}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

chequing_account.withdraw(chequing_account.get_service_charges())
savings_account.withdraw(savings_account.get_service_charges())
investment_account.withdraw(investment_account.get_service_charges())
investment_account_old.withdraw(investment_account_old.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(chequing_account)
print(savings_account)
print(investment_account)
print(investment_account_old)       