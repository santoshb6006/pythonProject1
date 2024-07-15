class Grandfather():
    home= "5 BHK"
    Gold= "100 KG"
    def own_property(self):
        print("Granfather's Propery")

class Father(Grandfather):
    car= "Mercedes Benz"
    tractu = "HMT"
    def own_property(self):
        print("Father's Property")

class Son(Father):
    bike= "Honda"
    car="BMW"
    def own_property(self):
        print("Son's Property")

father=Father()
print(father.own_property())#Father
print(father.Gold)#Grandfather
print(father.home)#Grandfather
print(father.tractu)#Father
print(father.car)#Father
print(father.Gold)#Grandfather
print(father.home)#Grandfather
#print(father.bike)#Grandfather
print("=========")

son=Son()
son.own_property()#Son
print(son.car)
print(son.bike)# Son
print(son.car)#Son
print(son.home)#GFather
print(son.car)#Father
print(son.Gold)#GFather
print(son.tractu)



