# Program 8:

from abc import *

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side=0):
        self.side = side
    
    def area(self):
        return self.side**2

    def perimeter(self):
        return 4*self.side

class Rectangle(Shape):
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

if __name__ == "__main__":
    side = int(input("Enter side of the Square: "))
    S = Square(side)
    print(f"Square:\nArea = {S.area()}\nPerimeter = {S.perimeter()}")

    length, breadth = [int(x) for x in input("Enter Length and Breadth of the Rectangle: ").split()]
    R = Rectangle(length, breadth)
    print(f"Rectangle:\nArea = {R.area()}\nPerimeter = {R.perimeter()}")
