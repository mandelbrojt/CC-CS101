from datetime import datetime


amount = float(input("How much money do you need to borrow?: "))
print()
monthly_term = int(input("In how many months do you want to finish paying your loan?: "))
print()
interest_rate = float(input("What's the annual interest rate they are charging you?\nPlease enter your answer without the '%' symbol: "))/100
print()
amortization_type = int(input("How would you like to pay each month?\n1. I want to pay principal and interest each month.\n2. I want to pay only interests each month.\n3. I want to pay principal and interest at the end of the loan term.\n Please input the option number (1, 2 or 3): "))
print()

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

periods = [i for i in range(loan.input_monthly_term+1)]
print(periods)

print(datetime.now())