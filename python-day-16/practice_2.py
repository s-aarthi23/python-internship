from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        pi=3.14
        r=float(input("Enter the radius:"))
        result= pi*r**2
        print("Area of the circle:",result)
circle=Circle()
circle.area()        


