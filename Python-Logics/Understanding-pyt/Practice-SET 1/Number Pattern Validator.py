number = input()

for i in range(len(number) - 1):
    if number[i] >= number[i + 1]:
        print("NO")
        break
else:
    print("YES")