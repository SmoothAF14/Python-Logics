password = input()
d = 0
u = 0
for i in password:
    if(i.isdigit()):
        d+=1
    elif(i.isupper()):
        u+=1
if(len(password) >= 8 and d>=1 and u>=1):
    print("STRONG")
else:
    print("WEAK")


