change = int(input("Enter the change : "))
lst = [1000, 500, 100, 50, 10, 5, 2, 1]
opt = []
nnum = 0

for i in lst:
    while change >= i:
        change -= i
        opt.append(i)
        nnum += 1
print(f"Minimum number of notes required: {nnum}")
print(f"Notes used: {opt}")

