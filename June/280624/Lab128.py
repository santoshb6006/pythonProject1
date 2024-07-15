class Person:
    name=input("Enter the name\n")
    age=input("Enter the age\n")

    def walk(self):
        a=20
        print("I'm a method")
        print(f"My age is, {self.age}")

pers=Person()
pers.walk()
#print(a)