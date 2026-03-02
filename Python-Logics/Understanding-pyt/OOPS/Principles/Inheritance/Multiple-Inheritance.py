#multiple parents
class father :
    def skills(self):
        return "Programming"
class mother:
    def talents(self):
        return "Singing"
class child(father,mother):
    pass 
c = child()
print(c.skills()) # Inherited method "skills" from the father class by using object c of the child class
print(c.talents()) # Inherited method "talents" from the mother class by using object c of the child class
# In this example, we have a child class that inherits from both the father and mother classes. The child class can access the methods of both parent classes, demonstrating multiple inheritance.

# Parent1
# Parent2
#     ↓
#    Child