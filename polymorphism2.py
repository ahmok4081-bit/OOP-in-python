from abc import ABC, abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius
        
class Square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2

        
class Triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
        
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super(). __init__(radius)
        

        



        
# the circle has 2 form is a Circle and the shape
shapes = [Circle(3), Square(9),Triangle(34), Pizza()]
for shape in shapes:
    print(shape.area)