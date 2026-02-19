#4
n = int(input("Enter value of N(less than 31) : "))
if (n>=31):
    print("The value shall be less than 31")
for i in range(n+1):
    print (f"2^{i} = {2**i}")

#5
n = int(input("Enter the vale of N : "))
harmonic = 0.0
for i in range (1,n+1):
    harmonic+= 1/i
print(f"The {n}th Harmonic Number is : {harmonic} ")