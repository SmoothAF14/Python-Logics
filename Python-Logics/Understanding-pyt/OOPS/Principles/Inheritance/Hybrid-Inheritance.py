class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show() # Inherited method "show" from class A by using object d of the class D
# In this example, we have a class A with a method "show". The classes B
# and C inherit from class A, and class D inherits from both B and C. The object d of class D can call the inherited method "show" from class A, demonstrating hybrid inheritance.

#        A      
#       / \
#      B   C
#       \ /
#        D