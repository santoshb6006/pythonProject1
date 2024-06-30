class Person:
    name = None
    age = None
    id = None
    phone_number = None


    def talking(self):
         print(f"Hello, my name is {self.name}")


    def walking(self):
        print(f"Hello, my name is {self.name}")


    def eating(self):
        print(f"Hello, my name is {self.name}")



    def sleeping(self):
        print(f"Hello, my name is {self.name}")


# Creating the object of the person class
dingya = Person()
dingya.name = "Sangya_Balya"
dingya.sleeping()
dingya.eating()

sangi = Person()
sangi.name = "Sangi_Bali"
sangi.age = 21
sangi.sleeping()
