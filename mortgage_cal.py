# Mortgage_Calculator V 1.0.0

class Emi:
    city = str(input('Enter City (Bangalore, Delhi, Mumbai, Chennai, Kolkata) ='))
    # at this Moment Only Main Indian Cities are defined
    home_value = float(input('Home Value ='))
    down_payment = float(input('Specify Down payment='))  # down payment is the payment that will be paid at start.
    interest_rate = float(input('Yearly Interest rate='))  # yearly interest rate.
    loan_term = float(input('Loan_Term in years ='))  # loan_Term is the period of total loan payment

    def cal_principal(self):
        stamp_duty = Emi.home_value * city_stamp_duty.get(Emi.city)
        registration_charges = 0.01 * Emi.home_value

        principal = Emi.home_value - Emi.down_payment + stamp_duty + registration_charges

        return principal, stamp_duty, registration_charges

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

principal_amount = Emi().cal_principal()[0]
stamp_duty_amount = Emi().cal_principal()[1]
reg_amount = Emi().cal_principal()[2]
monthly_emi_amount = Emi().cal_monthly_installment()[0]
number_of_installment = Emi().cal_monthly_installment()[1]

print()
print('In {} for the Home Value around {} Rs,\n the total principal amount is {} Rs. \n which includes stamp duty amount'
      ' {} Rs and registration charges {} Rs.'.format(Emi.city, Emi.home_value, principal_amount, stamp_duty_amount,
                                                     reg_amount))

print()
print('Now, if yearly Interest rate is {} % and Loan Term is {} years'.format(Emi.interest_rate, Emi.loan_term))
print('then you will need to pay monthly emi {} Rs.'.format(round(monthly_emi_amount,2)))




