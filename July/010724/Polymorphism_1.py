# Polymorphism
# This class represents a Dog object with a name and age attribute
# The polymorphism is implemented through the __str__ method, which returns a string representation of the object
# The object will behave differently at different stages
# Two types of polymorphism: static polymorphism (compile-time polymorphism, achieved through method overloading)
# and dynamic polymorphism (run-time polymorphism, achieved through method overriding)4
# Method overloading is doesn't exists in the polymorphism
class Shape():
    def areas(self):
        print("I am in shape, areas will be craeted")

    def area(self):
        print("Area of a shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.142 * self.radius * self.radius


shape1 = Rectangle(2, 3)
print(f"Area of a Rectangle is:", shape1.area())
print(shape1.areas())

shape2 = Circle(5)
print(f"Area of a Circle is:", shape2.area())

shape3 =Shape()
shape3.areas()
