# max two numbers
num1=int(input("enter a number1:\n"))
num2=int(input("enter a number2:\n"))
num3=int(input("enter a number3:\n"))
if num1>num2 and num1>num3:
    print("Num1 is the max",num1)
elif num2>num1 and num2>num3:
    print("Num 2 is max",num2)
elif num1==num2==num3:
    print("Num1 and num2 are equal")
else:
    print("Num 3 max",num3)
