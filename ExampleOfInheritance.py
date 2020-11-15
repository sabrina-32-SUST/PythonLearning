class Shape:
    def  __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def  area(self):
        print("I  am  area  method  of  shape  class")

class  Triangle(Shape):
    def area(self):
        result = 0.5*self.dim1*self.dim2
        print("Area  of  Triangle: ", result)


class Rectangle(Shape):
    def area(self):
        result =  self.dim1 * self.dim2
        print("Area  of  Rectangle: ", result)

ractangle = Rectangle(20,30)
ractangle.area()
triangle = Triangle(20,30)
triangle.area()