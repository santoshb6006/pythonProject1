def decorator(func):
    def wrapper():
        print("Wrapper started")
        func()
        print("Wrapper ended")
    return wrapper()


@ decorator
def say_hello():
    print("Hello123")

