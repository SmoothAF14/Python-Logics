from math import sqrt
print("Enter the three constants of the quadratic equation (ax^2 + bx + c = 0) : ")
a,b,c = int(input("a : ")),int(input("b : ")),int(input("c : "))
delta = pow(b,2) - 4*a*c
r1 = (-b + sqrt(delta)) / (2*a)
r2 = (-b - sqrt(delta)) / (2*a)
print(f"The roots of the equation are : {r1} and {r2}")