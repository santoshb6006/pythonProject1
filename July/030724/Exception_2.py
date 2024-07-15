try:
    a = int(input("Enter the number1:\n"))
    b = int(input("Enter the number2:\n"))
    c = a / b

    print("The result is",c)
except Exception as e:
    print("Please enter valid number:", e)
finally:
    print("End of the execution")