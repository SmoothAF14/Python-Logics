purc = int(input())
amt = 0.0
if purc >= 5000:
    amt = purc - purc*0.20
elif purc >= 2000:
    amt = purc - purc*0.10
elif purc >= 1000:
    amt = purc - purc*0.05
else:
    amt = purc  

print(f"{amt:.2f}")
