from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.raduis = radius
    def area(self):
        return 3.14 * self.raduis * self.raduis
    def perimeter(self):
        return 2 * 3.14 * self.raduis
c1 = circle(5)
print(c1.area())
print(c1.perimeter())
