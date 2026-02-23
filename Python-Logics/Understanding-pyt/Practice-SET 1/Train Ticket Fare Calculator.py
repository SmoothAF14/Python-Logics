dist = int(input())
age = int(input())
amt = dist*2
if age <12:
    amt -= amt*0.50
elif age >=60:
    amt -= amt*0.30
else :
    amt = amt
print(f"{amt:.2f}")
