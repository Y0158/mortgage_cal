# Mortgage_Calculator V 1.0.0

# The major variables in a mortgage calculation include, number of payments per year, total number of payments and
# the regular payment amount.

# More complex calculators can take into account other costs associated with a mortgage, such as local and
# state taxes, and insurance.

class Emi:
    city = str(input('Enter City ='))
    home_value = float(input('Home Value ='))
    down_payment = float(input('Specify Down payment='))  # down payment is the payment that will be paid at start
    interest_rate = float(input('Yearly Interest rate='))  # yearly interest rate
    loan_term = float(input('Loan_Term in years ='))  # loan_Term is the period of total loan payment
    # def __self__(self, city):  # country can be added here
    #     self.city = str(input('Enter City ='))
    #     self.
    #     # self.country = str(input('Enter Country ='))

    def cal_principal(self):
        stamp_duty = Emi.home_value * city_stamp_duty.get(Emi.city)
        registration_charges = 0.01 * Emi.home_value

        principal = Emi.home_value - Emi.down_payment + stamp_duty + registration_charges

        return principal     # principal amount

    def cal_monthly_installment(self):
        r1 = Emi.interest_rate / (100 * 12)     # r1 =  monthly interest rate
        n = Emi.loan_term * 12                  # number of total payment = loan term * 12.
        p = principal_amount   # this using Output from other method syntext to be checked

         # loop for calculating the the Monthly Payment
         # Formula for calculation is from the wiki.
    
        if Emi.interest_rate == 0:
            c = p / n
        elif Emi.interest_rate > 0:
            c1 = (r1 * p * ((1 + r1) ** n))
            c2 = ((1 + r1) ** n - 1)
            c = c1 / c2

        return c, n

city_stamp_duty = {'Bangalore': 0.03,'Delhi':0.06,'Mumbai': 0.05, 'Chennai': 0.07,'Kolkata': 0.05}

principal_amount = Emi().cal_principal()
print(principal_amount)

monthly_emi_amount = Emi().cal_monthly_installment()[0]
print(monthly_emi_amount)


# home_value = float(input('Home Value ='))  # total home Value
# down_payment = float(input('Specify Down payment='))  # down payment is the payment that will be paid at start
# interest_rate = float(input('Yearly Interest rate='))  # yearly interest rate
# loan_term = float(input('Loan_Term in years ='))  # loan_Term is the period of total loan payment
# monthly_payment , total_installment = monthly_installment(home_value, down_payment,
#                                                                             interest_rate, loan_term)
# print('Principal amount is {} Rs'.format(principal_amount))
# print('Total Monthly Payment is {} Rs'.format(monthly_payment))
# print('Processing Fees = {} Rs'.format(min(principal_amount*0.01,5000)))

