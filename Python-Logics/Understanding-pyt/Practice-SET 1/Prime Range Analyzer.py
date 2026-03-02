import math

a = int(input())
b = int(input())

count = 0
for num in range(a,b+1):
    if num>1:
        flag = 0
        for i in range (2,int(math.sqrt(num)+1)):
            if num%i == 0:
                flag = 1
                break
        if flag == 0:
            count+=1
print(count)