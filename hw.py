from math import *

# deg to rad
deg = int(input("please, enter degrees: "))

rad = radians(deg)
print(rad)

# rad to deg
rad = int(input("please, enter radians: "))

deg = degrees(rad)
print(deg)

# circle area
radius = int(input("please, enter the radius: "))

circle_area = pi * radius ** 2
print(circle_area)

# cylinder area
radius = int(input("please, enter the radius: "))
height = int(input("please, enter the height: "))

cylinder_area = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
print(cylinder_area)

# parallelogram area
side = int(input("please, enter the side: "))
height = int(input("please, enter the height: "))

parallelogram_area = side * height
print(parallelogram_area)

# sphere_area
radius = int(input("please, enter the radius: "))

sphere_area = 4 * pi * (radius ** 2)
print(sphere_area)

# sector area
radius = int(input("please, enter the radius: "))
deg = int(input("please, enter the value IN DEGREES: "))

sector_area = pi * (radius ** 2) * (deg / 360)
print(sector_area)

# quadratic equation roots
a8 = int(input("please, enter the a coefficient: "))
b8 = int(input("please, enter the b coefficient: "))
c8 = int(input("please, enter the c coefficient: "))

root_1 = (-b8 + sqrt((b8 ** 2) - (4 * a8 * c8))) / 2 * a8
root_2 = (-b8 - sqrt((b8 ** 2) - (4 * a8 * c8))) / 2 * a8
print(root_1, root_2)

# descriminant
a9_coeff = int(input("please, enter the a coefficient: "))
b9_coeff = int(input("please, enter the b coefficient: "))
c9_coeff = int(input("please, enter the c coefficient: "))

descriminant = (b9_coeff ** 2) - (4 * a9_coeff * c9_coeff)
print(descriminant)

# averages
a10 = int(input("please, enter number a: "))
b10 = int(input("please, enter number b: "))

arithmetic_mean = (a10 + b10) / 2
geometric_mean = sqrt(a10 * b10)
harmonic_mean = (2 * a10 * b10) / a10 + b10
quadratic_mean = sqrt(((a10 ** 2) + (b10 ** 2)) / 2)
print(arithmetic_mean, geometric_mean, harmonic_mean, quadratic_mean)

# trigonometric expression
deg = int(input("please, enter degrees: "))
rad = radians(deg)

trig_expression = sin(rad) + cos(rad) + (tan(rad) ** 2)
print(trig_expression)

# меня попросили написать