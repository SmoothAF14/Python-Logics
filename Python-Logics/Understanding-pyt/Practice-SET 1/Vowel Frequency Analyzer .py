sen = input()
cnt = 0
sens = sen.lower()
for i in sens:
    if i in 'aeiou':
        cnt+=1
print(cnt)