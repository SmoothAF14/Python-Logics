class grandparent():
    def land(self):
        print("Land from grandparent")
class parent(grandparent):
    def house(self):
        print("House from parent")
class child(parent):
    def car(self):
        print("Car from child")

c = child()
c.land() # Inherited method "land" from the grandparent class by using object c of the child class
c.house() # Inherited method "house" from the parent class by using object c of the child class
c.car() # method "car" from the child class by using object c of the child class

# In this example, we have a grandparent class with a method "land". The parent class inherits from the grandparent class and has its own method "house". The child class inherits from the parent class and has its own method "car". We can see that the child object can call both the inherited methods "land" and "house", as well as its own method "car", demonstrating multi-level inheritance.
# A → B → C