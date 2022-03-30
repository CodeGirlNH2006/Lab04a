import math

principal = 250000.0
annual_rate = 4.85
num_of_years = 30.0
monthly_payment = (annual_rate/100/12) * (1+(annual_rate/100/12))**(num_of_years*12)/((1+(annual_rate/100/12))**(num_of_years*12)-1)*principal
total_payments = monthly_payment*num_of_years*12
total_interest = total_payments - principal
print("Principal = " + str(principal))
print("Annual Rate = " + str(annual_rate))
print("Number of Years = " + str(num_of_years))
print("Monthly Payment = " + str(round(monthly_payment, 2)))
print("Total Payments = " + str(round(total_payments, 2)))
print("Total Interest = " + str(round(total_interest, 2)))