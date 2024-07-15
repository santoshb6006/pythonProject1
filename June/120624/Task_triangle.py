# Write a pgm to find the equal, isosceles, or scalene triangle from the given sides

def find_trianglestype(side1, side2, side3):
    if (side1 == side2 and side1 == side3 and side2 == side3):
        print("Equal's Triangle")
    elif (side1 == side2) or (side1 == side3) or (side2 == side3):
        print("Isosceles Triangle")
    else:
        print("scalene Triangle")


side1 = float(input("Size for Side 1\n"))
side2 = float(input("Size for Side 2\n"))
side3 = float(input("Size for Side 3\n"))

find_trianglestype(side1, side2, side3)
# find_trianglestype(85, 56, 85)
# find_trianglestype(58, 56, 85)