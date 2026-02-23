n = int(input("Enter the size of the array : "))
arr = []
count = 0
for x in range(n):
    arr.append(int(input(f"Enter element {x+1} : ")))
for i in range (n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] == 0:
                print(f"The triplet is : {arr[i]} , {arr[j]} , {arr[k]}")
                count+=1

print(f"The number of triplets are : {count}")