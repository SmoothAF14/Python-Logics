salary = float(input())
late = int(input())
absent = int(input())


if late > 10:
    salary -= salary*0.10
elif late > 5:
    salary -= salary*0.05


if absent > 2 :
    salary -= salary*0.05
print(f"{salary:.2f}")