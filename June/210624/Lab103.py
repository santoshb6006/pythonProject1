#Decorator

def decorator(func):
    def wrapper():
        print('함수 시작')
        func()
        print('함수 ���')
    return wrapper
@decorator
def hello():
    print('hello')

hello()