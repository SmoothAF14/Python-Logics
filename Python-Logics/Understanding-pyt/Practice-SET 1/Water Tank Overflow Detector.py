n = int(input())
inflo = list(map(int, input().split()))

capacity = 1000
total = 0

for i in range(n):
    total += inflo[i]
    if total > capacity:
        print(i+1)
        break