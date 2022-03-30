import math

p = 250000
r = 4.85
ny = 30
nm = ny * 12
mr = r/(12*100)
monthlypayment = p * mr * ((1+mr)**ny)/((1+mr)**ny - 1)
print(monthlypayment)