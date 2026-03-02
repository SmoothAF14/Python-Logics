n =int(input())
pali = n
rev = 0
digit = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n//=10
if rev == pali:
    print("PALINDROME")
else:
    print("NOT PALINDROME")