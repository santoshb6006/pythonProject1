#Multilevel Inheritance
class Father():
    gold = "100 kg"
    land = "100 acres"

    def car(self):
        return "Father's Car BMW"


class Son(Father):
    only_land = "50 acres"

    def bike(self):
        return "Son's Local bike"


class Grandson(Son):
    only_land = "Bhikari"

    def scooter(self):
        return "Its scooter"


pare = Grandson()
pare.only_land
print(pare.scooter())
print(pare.bike())
print(pare.gold)
print(pare.land)
