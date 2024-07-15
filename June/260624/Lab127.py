class Student:

    def __init__(self):
        self.name= input("Enter the name\n")
        self.age= input("Enter the age\n")
    def display(self):
        print(f"my name is,{self.name} and age is,{self.age}")

stud = Student()
stud.display()