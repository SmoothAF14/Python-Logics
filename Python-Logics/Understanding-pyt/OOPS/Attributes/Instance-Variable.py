class dog:
    def __init__(self, name, age):
        self.name = name        #self.name stores the name inside that object
        self.age = age
    
d1 = dog("tommy", 5)
d2 = dog("timmy", 3)
print(f"Name of the dog is {d1.name} and age is {d1.age} ")
print(f"Name of the dog is {d2.name} and age is {d2.age} ")