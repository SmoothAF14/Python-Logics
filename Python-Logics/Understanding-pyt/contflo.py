#if-elif-else
marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(grade)

#nested if 
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")


#Ternary conversion
num = 5
result = "Even" if num % 2 == 0 else "Odd"

