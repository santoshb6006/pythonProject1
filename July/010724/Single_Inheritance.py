# Inheritance
# Inheriting the properties of a class into a child class
# Types of inheritance
# 1.Single inheritance
# 2.Multiple inheritance
# 3.Multilevel inheritance
# 4.Hierarchical inheritance
# 5.Hybrid inheritance

class Father:
    def asth(self):
        return "Hello"



class Santosh(Father):
    def my_prop(self):
        return "Its my Property"


parent = Santosh()
parent.asth()
print(parent.asth())
print(parent.my_prop())