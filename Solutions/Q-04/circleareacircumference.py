# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 4. Write a Python program to calculate the area and circumference of a circle.


import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
