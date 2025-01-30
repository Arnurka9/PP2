
"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    def __init__(self):
        self.areaShape = 0
    
    def area(self):
        print(self.areaShape)
    
    
class Square(Shape):
    def __init__(self, length: float):
        super().__init__()  #useless thing
        self.length = length

    def area(self):
        print(self.length ** 2)


"""
Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width.
The Rectangle class has a method which can compute the area.
"""

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        print(self.width * self.length)


anyShape = Shape()
anyShape.area()

my_square = Square(4)
my_square.area()
 
my_rectangle = Rectangle(4, 5)
my_rectangle.area()


