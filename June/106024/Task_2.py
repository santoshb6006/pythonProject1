# Question_1 Develop a Python script that calculates the square and
# cube of a given number. num = 2 sq - 4, c = 8

num=int(input("Enter num\n"))
square=num**2
cube=num**3
print("Square of the Given Number",square)
print("Cube of the Given Number:", cube)

# Create a program that takes two numbers as input and prints whether the
# first number is greater than, less than, or equal to the second number.
num1=int(input("Enter the num1:\n"))
num2=int(input("Enter the num2:\n"))

if num1>num2:
    print("Num1 is greater")

elif num1<num2:
    print("Num1 is less than num2")
else:
    print("Num1 is equal to the num2")