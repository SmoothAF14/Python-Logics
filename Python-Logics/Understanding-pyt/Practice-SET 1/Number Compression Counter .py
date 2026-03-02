num = int(input())
cnt = 0
while num%2==0:
    cnt+=1
    num//=2
print(cnt)