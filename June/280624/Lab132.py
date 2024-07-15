class Car:
    name=None

    def __init__(self):
        self.public_var="public"
        self._protected_var="protected"
        self.__private_var="private"

    def public_method(self):
        if self.__private_var=="123":
            print("123")
        print("I'm publicly allowed")
    def _protected_method(self):
        print("I'm a protected method")

    def __private_method(self):
        print("I'm a private method")



zen=Car()
zen.public_method()
zen.public_var="I got Zen"
