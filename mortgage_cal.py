# Mortgage_Calculator V 1.0.0

# The major variables in a mortgage calculation include loan principal, balance, periodic
# compound interest rate, number of payments per year, total number of payments and the regular payment amount.
# More complex calculators can take into account other costs associated with a mortgage, such as local and
# state taxes, and insurance.

# Output requirements

# Variables

# defining the function for Emi

def monthly_installment(home_value, down_payment, interest_rate, loan_term):
    p = home_value - down_payment  # p =  principal amount
    r1 = interest_rate / (100 * 12) # r1 =  monthly interest rate
    n = loan_term * 12  # number of total payment = loan term * 12.
    # loop for calculating the the Monthly Payment
    # Formula for calculation is from the wiki.
    if interest_rate == 0:
        c = p / n
    elif interest_rate > 0:
        c1 = (r1 * p * ((1 + r1) ** n))
        c2 = ((1 + r1) ** n - 1)
        c = c1 / c2
    return c, p, n


home_value = float(input('Home Value ='))  # total home Value
down_payment = float(input('Specify Down payment='))  # down payment is the payment that will be paid at start
interest_rate = float(input('Yearly Interest rate='))  # yearly interest rate
loan_term = float(input('Loan_Term in years ='))  # loan_Term is the period of total loan payment


print('Principal amount is {principal_amount}'.format(principal_amount = p))
print('Total Monthly Payment is {monthly_payment}'.format(monthly_payment = c))

