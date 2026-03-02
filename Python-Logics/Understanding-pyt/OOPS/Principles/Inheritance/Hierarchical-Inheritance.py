class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def sound(self):
        print("Barking")

class Cat(Animal):
    def sound(self):
        print("Meowing")

d = Dog()
c = Cat()

d.sound() #polymorphism: same method name "sound" but different implementation in Dog and Cat class
c.sound()

d.eat()#inherited method "eat" from the Animal class by using object d of the Dog class
c.eat()#inherited method "eat" from the Animal class by using object c of the Cat class

# In this example, we have a base class "Animal" with a method "eat". The "Dog" and "Cat" classes inherit from the "Animal" class and have their own implementation of the "sound" method. We can see that both the Dog and Cat objects can call the inherited "eat" method, demonstrating hierarchical inheritance.
#        Parent
#       /      \
#    Child1   Child2