# Question#1
# Explain the difference between the = operator and the == operator in Python?
#A_The equal operator(=) is used to assign a value to a variable.
age=12
print(age) # 12
# basically it check for the what value is assigned to o the variable and print it.

#The double equal operator(==) is used to compare two values and return a boolean value.
#(==) will check for the value assigned to the variable is correct or not wrt what is given in the condition.
age=12
print(age==12)# True
print(age==21) # False

#Question#2
# What does the ** operator do in Python, and how is it used?
#The ** operator is used to raise a number to a power. ex- 2^3 = 8
# #It is commonly used to calculate powers in mathematics.
print(2**2) # 4
print(2**3) # 8
#Question#3
# What does the ^ operator do in Python, and in what context is it commonly used?
#The ^ operator is used to perform bitwise XOR operation on two numbers.
#It is commonly used in cryptography to encrypt and decrypt data.
print(2^3) # 1
print(3^2) # 1
#Question#4
# What is the difference between the and and or operators in Python?
#The and operator returns "True" if both the operands are True else it will return "False".
#The or operator returns "True" if either of the operands is True else it will return "False"..
#And Operator
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or True) # True
#Or Operator
print(True or False) # True
print(False or True) # True #etc
