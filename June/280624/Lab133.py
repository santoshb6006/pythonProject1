class Myclass:
    def __init__(self):
        self.name="Santosh"
        self.email="asd@gmail.com"
    def public_fn(self):
        print("public fn()")

    def __private_fu(self):
        print("__private func() you can only access me via anther method")

    def _protected(self):
        print("Its a protected")
        print(self.email)

cl=Myclass()
cl.email
cl.public_fn()
