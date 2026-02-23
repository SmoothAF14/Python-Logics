def ctof(c):
    f = (c * 9/5) + 32
    return f
def ftoc(f):
    c = (f - 32) * 5/9
    return c

cof = int(input("Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius: "))
if cof == 1:
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c} degrees Celsius is equal to {ctof(c):.2f} degrees Fahrenheit.")
elif cof == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f} degrees Fahrenheit is equal to {ftoc(f):.2f} degrees Celsius.")