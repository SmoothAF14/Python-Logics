ini = input()
bin = int(ini)
dec = 0
length = len(ini)
cnt = length-1
for i in ini:
    if i == '1':
        dec += 2**cnt
    cnt -= 1
print(dec)  

