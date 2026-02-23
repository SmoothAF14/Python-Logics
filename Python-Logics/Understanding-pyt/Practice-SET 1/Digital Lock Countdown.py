num = int(input())
while num>=10:
    digsum = 0
    temp = num
    while temp>0:
        digsum += temp%10
        temp//=10
    num = digsum
print(num)