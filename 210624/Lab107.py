def fun_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__} with {args} "
def add(a,b,c,d):
    return a+b

add(2, 3, 4, 5)
