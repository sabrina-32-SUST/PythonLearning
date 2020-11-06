#Area  of  a Shape

base =  float(input("Enter  Base = "))
height = float (input("Enter Height = "))
length = float (input("Enter Length = "))
width = float (input("Enter Width = "))
radius = float (input("Enter Radius = "))
angle  = int(input("Enter Angle = "))

area = 0.5 *base*height
print("Area of Triangle : " , area)

area = length*length
print("Area of Square : " , area)

area = width*height
print("Area of Rectangle : " , area)

area = base* height
print("Area of Parallelogram : " , area)

area = .5*(length+base)*height
print("Area of Trapezoid  : " , area)

area = 3.1416* radius*radius
print("Area of Circle  : " , area)

area = 3.1416*length*base
print("Area of Ellipse  : " , area)

area = 0.5*radius*radius*angle
print("Area of Sector  : " , area)









