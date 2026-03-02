#6
n = int(input("Enter number to find prime factors for : "))
divisor = 2
factors = []
while n > 1:
    while n%divisor == 0 :
        factors.append(divisor)
        n//=divisor
    divisor+=1
print(set(factors))
