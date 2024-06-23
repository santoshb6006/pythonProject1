num=int(input("Enter the number\n"))
fact=1
for i in range(1,num+1):
    fact=(fact*i)

print("The factorial of the number is", fact)

# 2nd method
def factorial(num1):
    fact=1
    for i in range(1, num1+1):
        fact*=i
        print(fact)
    return fact

num1=int(input("Enter the num1\n"))
print("The factorial of the",num1,"is", factorial(num1))