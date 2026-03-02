class Math:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
    @staticmethod
    def add( x,y):
        return x+y
    @staticmethod
    def multiply(x,y):
        return x*y
d1 = Math(5,10)
print(d1.add(d1.x,d1.y))         #print(Math.add(5, 3))  # calling the static method using the class name
print(d1.multiply(d1.x,d1.y))    #print(Math.multiply(5, 3))  # calling the static method using the class name
