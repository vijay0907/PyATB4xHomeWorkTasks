#Write a Python program to calculate
# the area of a circle given its radius using the formula
# area=3.14 x r^2 (Pie = 3.14)

import math
from xmlrpc.client import MultiCall

pi_value = math.pi
print("PI Value is ",pi_value)

radius = float(input("Enter the radius of the circle : "))

area = math.pi*math.pow(radius,2)
print(f"Area of the circle is: {area:.2f}")