def my_deco(func):
    def wrapper():
        print("Before calling the Function")
        func()
        print("After calling the function")

   # return wrapper()
    return wrapper


@my_deco
def san_hello():
    print("Hello San")
san_hello()