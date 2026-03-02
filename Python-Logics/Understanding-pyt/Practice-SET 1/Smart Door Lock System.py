pin = input()
flag = 0
for i in range (0,3):
    sol = input()
    if sol == pin:
        print("ACCESS GRANTED")
        flag = 1
        break   
if flag == 0:
    print("ACCESS DENIED")
