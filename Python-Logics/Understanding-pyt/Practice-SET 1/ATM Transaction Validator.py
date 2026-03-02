ibal = int(input("Enter inital balance : "))
nnum = int(input("Enter number of withdrawals : "))
for i in range(nnum):
    w = int(input())
    if ibal >= w and w%100 == 0:
        ibal -= w
        print("SUCCESS")
    else:
        print("FAILED")
        
print(f"Final Balance is : {ibal}")

