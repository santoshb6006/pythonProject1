class Dog:
    name = None
    id = None

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id


    def sleep(self):
        print("Its a Lab for sleep")


dog1 = Dog(name="Chinns", id="4056")
dog2 = Dog(name="Fhinns", id="321")

print(f"Dog1 name is,{dog1.name} and id is {dog1.id}")
print(f"Dog1 name is,{dog2.name} and id is {dog2.id}")

dog1.sleep()
dog2.sleep()