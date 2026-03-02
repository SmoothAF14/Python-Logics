def dayofweek(m,d,y):
    y0 = y-(14-m)//12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m+12*((14-m)//12)-2
    d0 = (d+x+31*m0//12)%7
    return d0
m = int(input("Enter month: "))
d = int(input("Enter day: "))
y = int(input("Enter year: "))

print("Day of week (0=Sunday,...6=Saturday):", dayofweek(m, d, y))