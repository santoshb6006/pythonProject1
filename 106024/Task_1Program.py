# To calculate the area of a circle

def area_of_circle(radius):
    import math
    area = math.pi * radius * radius # Core logic of the program
    return area # reaturning the area
radius =float(input("Enter the radius of a circle\n"))# user input for
print(area_of_circle(radius))

#Script for to find square and cube of number
def square_cube_of_a(num):
    #sq= num**2
    cube=num**3
    return sq,cube
num=int(input("Enter the num\n"))
print(square_cube_of_a(num))

# Script to find the greter than less than and equal to
def greater_less_equal_to(num1,num2):
    if num1>num2:
        print("The Num1 is greater than the Num2->",num1)
        return num1
    elif num1<num2:
        print("The Num1 is lesser than the Num2->", num1,num2)
        return  num2
    else:
        print("Both numbers are equal->",num1,num2)
        return num1,num2

num1=int(input("Enter the num1:\n"))
num2=int(input("Enter the num2:\n"))
#print(greater_less_equal_to(num1,num2))
result=greater_less_equal_to(num1, num2)
print(result)