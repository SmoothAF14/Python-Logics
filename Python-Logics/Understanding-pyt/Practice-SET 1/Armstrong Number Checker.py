num = int(input())
n = len(str(num))
fin = num
sum = 0

for i in range(num):
    digit = int(num%10)
    sum = sum+(digit**n)
    num//=10
if (sum==fin):
    print("YES")
else:
    print("NO")