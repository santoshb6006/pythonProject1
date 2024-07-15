# Factorial with while loop
n = 5
factorial = 1
while n > 0:
    factorial = factorial * n
    n = n - 1

print(factorial)
print("=====================")
# Factorial with for loop
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)
