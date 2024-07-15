# Recursion
#recurion is a function that calls itself to solve a problem
#Base case and recursive case
#factorial of a number
#5! = 5*4*3*2*1 = 120

def factorial(n):
    #n=n-1
   #base case
   if n==1 or n==0:
      return 1
   #Recursive case
   else:
      return n*factorial(n-1)
print(factorial(5))