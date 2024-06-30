import time
def log_noter_deacorator(func):
    def wrapper():
        print("Starting")
        start = time.time()
        func()
        print("Ending")
        end=time.time()
        print(f"Total time {end-start}")
    return wrapper()

@log_noter_deacorator

def log_function():
    time.sleep(5)
    print("Note all logs")
