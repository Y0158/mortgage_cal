# Mortgage_Calculator V 1.0.0

# The major variables in a mortgage calculation include loan principal, balance, periodic
# compound interest rate, number of payments per year, total number of payments and the regular payment amount.
# More complex calculators can take into account other costs associated with a mortgage, such as local and
# state taxes, and insurance.

# Output requirements

# Variables
H = float(input('Home Value ='))                  # H = total home Value
Down_payment = float(input('Specify Down payment='))  # down payment is the payment that will be payied at start
P = H - Down_payment                                 # p =  principal amount
r = float(input('Yearly Interest rate='))         # r = yearly interest rate
r1 = r / ( 100 * 12 )                             # r1 =  monthly interest rate
Loan_Term = float(input('Loan_Term in years ='))  # Loan_Term is the period of total loan payment
N = Loan_Term * 12                                # number of monthly payment for it is set to 12.

# loop for calculating the the Monthly Payment
# Formula for calculation is from the wiki.
if r == 0:
    c = P / N
elif r > 0:
    c1 = (r1 * P* ((1 + r1)**N))
    c2 = ((1 + r1)**N - 1)
    c = c1 / c2

print('Principal amount is {}'.format(round(P,0)))
print('Total Monthly Payment is {}'.format(round(c,2)))

