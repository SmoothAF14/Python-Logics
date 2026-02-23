def monthlypayment (p,y,r):
    n = 12*y
    r = r/(12*100)
    pay = (p*r)/(1-(1+r)**(-n))
    return pay

p = float(input("Enter the principal amount: "))
y = int(input("Enter the number of years: "))
r = float(input("Enter the annual interest rate:"))
print(f"Monthly payment is: {monthlypayment(p,y,r):.2f}")