#실습 2.1

radius = float(input("Enter the radius : " ))

from math import pi
area = round(pi * radius ** 2, 1)
print("The area of a circle with radius", radius, "is", area)
