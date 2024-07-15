class Father():
    def home_self(self):
        print("This is from my home")
    def father_money(self):
        print("This is a father's money")
    def father_property(self):
        print(" Father")


class Mother():
    def mother_money(self):#Methos Resolution Order MRO
        print("This is a Mother's Money")

    def mother_home(self):
        print("This money taken from mom")
    def mother_property(self):
        print(" Mother")



#class Son(Father, Mother):
class Son(Mother, Father):
    pass
    # def own_property(self):
    #     print("Begging to parents")

child = Son()
child.mother_property()
child.father_property()
(child.mother_home())
(child.father_money())
(child.mother_money())
#(child.own_property())
print("=========")