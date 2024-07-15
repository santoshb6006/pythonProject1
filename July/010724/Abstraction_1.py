#Abstract Method
from abc import ABC, abstractmethod
# Hiding the details and showing only the essential features of an object
class Animal(ABC):
    def __init__(self,name):
        self.name =name

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "BOW BOW!"
class Cat(Animal):
    def sound(self):
        return "MEOW MEOW!"

# class Camel(Animal):#TypeError: Can't instantiate abstract class Camel without an implementation for abstract method 'sound'
#         pass

dog =Dog("Doggy")
print(dog.sound())

cat=Cat("Catty")
print(cat.sound())

# camel=Camel("Camel")
# print(camel.sound())