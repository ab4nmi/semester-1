# Week 1.6, Session 1: Task 3
# Week 1.6, Session 1: Task 3
from point import Point
from shapes import Circle

# make circle
c1 = Circle(2.5, Point(0.0, 0.0))
print(c1)

# print area and perimiter
print("Area =", round(c1.area(), 3))
print("Perimeter =", round(c1.perimeter(), 3))

# move it
print("Moving the circle")
c1.set_position(Point(2.0, 3.0))
print(c1)

# change colour
c1.set_colour("blue")
print(c1)
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
