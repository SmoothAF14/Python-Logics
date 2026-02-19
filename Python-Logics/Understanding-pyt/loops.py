# #range
# range(5)        # 0 to 4
# range(1, 5)     # 1 to 4
# range(1, 10, 2) # 1,3,5,7,9

# #enumerate 
# fruits = ["apple", "banana", "cherry"]

# for index, value in enumerate(fruits):
#     print(index, value)

# #while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# #for loop
# for i in range(5):
#     if i == 10:
#         break
# else:
#     print("Loop completed without break")

# #factorial 
# num = int(input("Enter a Number :"))
# i = 1
# fact = 1
# for i in range(1,num+1): #range always starts with 0 
#     fact = fact *i

# print(f"The Factorial is {fact}")

#armstrong 
num = int(input("Enter a Number :"))
n = len(str(num))
fin = num
sum = 0

for i in range(num):
    digit = int(num%10)
    sum = sum+(digit**n)
    num//=10
if (sum==fin):
    print(f"The sum is {sum}, and hence is it an armstrong number")
else:
    print(f"The sum is {sum}, and hence is it not an armstrong number")
        

