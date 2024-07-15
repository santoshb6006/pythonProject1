#Exception
# It is an event triggered during the execution which stops the execution suddenly abruptly, which should be handled using try and except method.

a= int(input("Enter the number1:\n")) # if we enter 10:- ValueError: invalid literal for int() with base 10: 'asdasd'
b= int(input("Enter the number2:\n"))
c=a/b
print("End of the program with below result")
print(c)