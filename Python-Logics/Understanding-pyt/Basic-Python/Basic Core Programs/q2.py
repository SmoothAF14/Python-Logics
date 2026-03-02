#2
import random
n = int(input("Enter number of coin flips : "))
if n <= 0:
    print("Number of flips should be a positive integer")
head = 0
tail = 0
for i in range(n):
    if random.random() < 0.5:
        tail+=1
    else:
        head+=1

print(f"The odds of getting heads is {head/n*100}%, and the odds of getting tails is {tail/n*100}%")
