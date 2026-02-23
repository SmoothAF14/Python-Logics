#3
yearstr=input("Enter a year : ")
if(len(yearstr) !=4 ):
    print("Year should be a 4 digit number")
year= int(yearstr)
if (year%4==0 and year%100 != 0) or (year%400 == 0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")