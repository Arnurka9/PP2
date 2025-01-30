
"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x},{self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 )**0.5

point_1 = Point(1,2)
point_2 = Point(3,4)

point_1.show()
point_2.show()

point_1.move(5, 6)
point_1.show()

print(point_1.dist(point_2))
