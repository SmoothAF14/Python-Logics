arr = []
flag = 0
avg = 0

for i in range(0, 5):
    arr.append(int(input()))

for i in range (0,5):
    if arr[i] < 35:
        flag = 1
        break
    avg += arr[i]

if(avg//5 >= 75 and flag!= 1):
    print("DISTINCTION")
elif(flag==1):
    print("FAIL")
else:
    print("PASS")


