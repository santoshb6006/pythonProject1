# Recursion
# It's aprogramming technique where a function will call itself in order to solve the problem.

# Key Concept
# 1. Base Condition
# 2. Recursive Case

num=int(input("Enter the num for fact\n"))

fact=0

def factorial(num):
     #Base Case
    if num==0 or num==1:
        return 1
    #Recursive function
    else:
        return num * factorial(num-1)



print(factorial(num))

