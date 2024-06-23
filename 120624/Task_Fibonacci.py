# Write a program to find the fibonacci series
# Here we do the addition of the successor number with the predecessor
# let's take a, b=0,1 then we store the result in the series list
def fibonacci(n):
    num1, num2= 0,1
    result=[]

    for _ in range(n):
        result.append(num1)
        num1,num2=num2,num1+num2
    return result


# Here we print the fibonacci series up to 10 terms.
num=int(input("Enter the number\n"))
#print(fibonacci(num))
fib_resu=fibonacci(num)
print(f"Fibonacci series up to {num} terms: { fib_resu}")




