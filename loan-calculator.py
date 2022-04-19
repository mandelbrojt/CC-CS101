# Import required packages
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

# Ask the user to input the loan terms
amount = float(input("How much money do you need to borrow?: "))
print()
monthly_term = int(input("In how many months do you want to finish paying your loan?: "))
print()
interest_rate = float(input("What's the annual interest rate they are charging you?\nPlease enter your answer without the '%' symbol: "))/100
print()
amortization_type = int(input("How would you like to pay each month?\n1. I want to pay principal and interest each month.\n2. I want to pay only interests each month.\n3. I want to pay principal and interest at the end of the loan term.\n Please input the option number (1, 2 or 3): "))
print()

# Create a class for loans and include a description when an object is created
class Loan:
    def __init__(self, input_amount, input_monthly_term, input_interest_rate, input_amortization_type=1):
        self.input_amount = amount
        self.input_monthly_term = monthly_term
        self.input_interest_rate = interest_rate
        self.input_amortization_type = amortization_type
    
    # Give a description of the loan main parameters
    def __repr__(self):
        description = "Your loan of {loan_amount} dollars will be paid in {term} months and ".format(loan_amount=amount, term=monthly_term)
        if amortization_type == 1:
            description += "you will pay interest and principal in each month."
        elif amortization_type == 2:
            description += "you will have to pay the interest each month.\nThe principal will be paid in the last month of the term."
        elif amortization_type == 3:
            description += "the interest and principal will be paid at maturity."
        return description

print("Here is a brief description of your loan: \n")
loan = Loan(amount, monthly_term, interest_rate, amortization_type)
print(loan)

# Use list comprehension to store each period number of the loan term
periods = [i for i in range(1,loan.input_monthly_term+1)]
print(periods)

# Get the current date to use it as the initial date of the loan
todays_date = datetime.today()

# Iterate through each period and add its value as the number of months to increase to the initial date
# Append each result as a string in the list comprehension
dates = [(todays_date + relativedelta(months=period)).strftime("%Y-%m-%d") for period in periods]
print(dates)

# Calculations for principal and interest payments
if loan.input_amortization_type == 1:
    interest = []
    principal = []
    payments = [round((loan.input_amount * loan.input_interest_rate/12) / (1 - ((1 + loan.input_interest_rate/12) ** (-loan.input_monthly_term))),4) for i in range(1,loan.input_monthly_term+1)]
    balance = []
    
    interest.append(round(loan.input_amount * loan.input_interest_rate/12,4))
    principal.append(round(payments[0]-interest[0],4))
    balance.append(round(loan.input_amount - principal[0],4))
    
    for i in range(5):
        interest.append(round(balance[i] * loan.input_interest_rate/12,4))
        principal.append(round(payments[i] - interest[i + 1],4))
        balance.append(round(balance[i] - principal[i + 1],4))

# Calculations for interest payment only
elif loan.input_amortization_type == 2:
    interest = []
    principal = []
    payments = []
    balance = []
    for period in periods:
        interest.append(round((loan.input_amount * loan.input_interest_rate/12)))
        if period == loan.input_monthly_term:
            principal.append(loan.input_amount)
            payments.append(round((loan.input_amount * loan.input_interest_rate/12) + loan.input_amount,2))
            balance.append(0)
        else:
            principal.append(0)
            payments.append(round(loan.input_amount * loan.input_interest_rate/12))
            balance.append(loan.input_amount)

# Calculations for payments at maturity
elif loan.input_amortization_type == 3:
    interest = []
    principal = []
    payments = []
    balance = []
    for period in periods:
        if period == loan.input_monthly_term:
            interest.append(loan.input_amount * loan.input_interest_rate/12)
            principal.append(loan.input_amount)
            payments.append(loan.input_amount + loan.input_amount * loan.input_interest_rate/12)
            balance.append(0)
        else:
            interest.append(0)
            principal.append(0)
            payments.append(0)
            balance.append(loan.input_amount)

# Create a dictionary to assign to each key its corresponding list
amortization_dict = {'Period': periods, 'Date': dates, 
                     'Interest': interest, 'Principal': principal,
                     'Total Payment': payments, 'Balance': balance}

# Use the previous dictionary to create a dataframe
amortization_df = pd.DataFrame(amortization_dict)
print(amortization_df)