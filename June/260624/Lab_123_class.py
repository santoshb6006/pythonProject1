class Person:
    # Attributes
    name = None
    id = None
    age = None
    ph_no = None


    # Behavior
    def sleep(self):
        print(f"I'm sleeping fellow, {self.name}")

    def walk(self):
        print(f"I'm walking,{self.name}")
        print(f" My age is ,{self.age}")

    def bark(self):
        print(f"I'm walking,{self.name}")
        print(f" My id is ,{self.id}")


# Creating object of the person

sur = Person()
sur.name = "Pandya"
sur.sleep()

rit = Person()
rit.id = "123"
rit.bark()

din = Person()
din.ph_no = "987456123"
din.age=213
din.walk()
