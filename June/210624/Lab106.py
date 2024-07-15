import time

def decorator1(func):
    def wrapper():
        print("Decorations starts")
        start=time.time()
        func()
        print("Decorations ends")
        end=time.time()
        print(f"Total time, {end-start}")
        print(f"Total time, {end+start}")
    return wrapper()
def decorator2(func):
    def wrapper():
        print("Decorations2 starts")
        start1=time.time()
        func()
        print("Decorations2 ends")
        end1=time.time()
        print(f"Total time, {end1-start1}")
        print(f"Total time, {end1+start1}")
    return wrapper()
@decorator1

def say_hello():
    time.sleep(1)
    print("Hello!")
@decorator2

def say_goodbye():
    time.sleep(2)
    print("Goodbye!")
