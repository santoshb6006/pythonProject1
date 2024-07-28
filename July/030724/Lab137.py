def fibonacci_series(num):
    fib = []
    a, b = 0, 1
    while len(fib) < num:
        fib.append(a)
        a, b = b, a + b  # a=b and b=a+b
    return fib

num=10
fibb = fibonacci_series(num)
print(fibb)


