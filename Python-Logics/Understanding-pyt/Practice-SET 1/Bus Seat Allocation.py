seats = 40
n = int(input())
for i in range(n):
    a = int(input())
    if a<=seats:
        print("CONFIRMED")
        seats-=a
    else:
        print("WAITING")

