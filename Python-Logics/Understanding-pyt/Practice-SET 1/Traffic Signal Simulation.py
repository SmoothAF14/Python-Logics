time = int(input())
t = time%90

if 1<= t <= 30:
    print("Red")
elif 31<= t <= 45:
    print("Yellow")
else:
    print("Green")


