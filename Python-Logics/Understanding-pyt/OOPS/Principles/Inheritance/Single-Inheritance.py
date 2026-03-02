class animal :
    def eat(seld):
        print("Eating...")
class dog(animal):
    def bark(self):
        print("Woof!")
d1 = dog()
d1.eat() # Inherited method "eat" from the animal class by using object d1 of the dog class 
d1.bark()
# In this example, we have a base class "animal" with a method "eat". The "dog" class inherits from the "animal" class and has its own method "bark". We can see that the dog object can call both the inherited "eat" method and its own "bark" method, demonstrating single inheritance.

# Parent → Child

