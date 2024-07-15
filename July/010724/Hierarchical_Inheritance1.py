class Father():
    house= "5 BHK house"
    def own_propertyy(self):
        print("Father's property")

class First_son(Father):
    own_car = "Mercedes Benz"
    def own_property(self):
        print("First son's property")

class Second_son(Father):
    own = "Local car"
    def own_prop(self):
        return "cycle only"

class Thirs_son(Father):
    own = "Big Big business"
    def own_propi(self):
        print("Thirs son's property")


sant = Thirs_son()
print(sant.own_propi())
print(sant.house)
print(sant.own_propertyy())
print("\n")
sant = Second_son()
print(sant.own_prop())
print(sant.own)
print(sant.own_propertyy())
print(sant.house)
print("\n")
sant = First_son()
print(sant.own_car)
print(sant.own_property())
print(sant.house)


