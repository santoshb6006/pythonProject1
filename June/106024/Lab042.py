# program to calculate the are of a circle
# input radius =
# output area formula = pi * r * r
import math

pi = 3.14159

rad = float(input("Enter the radius of a circle\n"))
area = pi*(rad*rad)
print("The Area for an entered radius is:",area)
area1= math.pi*rad*rad
print("area1",area1)

print(math.pi*(float(input("Enter the radius of a circle\n"))**2))