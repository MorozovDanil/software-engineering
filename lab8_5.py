class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = 7
circle = Circle(r)
print(circle.area())

l = 5
w = 7
rectangle = Rectangle(l, w)
print(rectangle.area())
