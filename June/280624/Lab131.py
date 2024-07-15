# Encapsulation
# Wrapping / bind the data variables with the methods
# Data menmbers/ Class variables
#Methods- Def, Function within the class
# Wrapping or binding the data variables with the methods-Encapsulation

#Hide the data members (Class variables, instance variables) by using only the methods
class Car:
    def __init__(self):
        print("I'm called when an object is created")

    def change_pwd(self):
        self.pwd="1234"
        return pwd

xuv=Car()
xuv.pwd="4653"




