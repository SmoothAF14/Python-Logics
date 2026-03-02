from math import sqrt
x = int(input("Enter the x coordinate : "))
y = int(input("Enter the y coordinate : "))

distance = sqrt(pow(x,2) + pow(y,2))
print(f"The distance from the point ({x},{y}) to the origin (0,0) is : {distance}")