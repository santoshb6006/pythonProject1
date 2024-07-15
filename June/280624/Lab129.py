class Car:
    name = None
    make = None
    model = None
    color = None


    def  __init__(self,name,make,model,color):
        self.name = name
        self.make = make
        self.model = model
        self.color = color

    def start_engine(self):
        print("Starting a car with the name " +self.name)
        print("Starting a car with the make "+self.make)
        print("Starting a car with the model " +self.model)
        print("Starting a car with the color " +self.color)

    def xuv_mahi(self):
        print("Starting a car with the name"+self.name)
        print("Starting a car with the make"+self.make)
        print("Starting a car with the model"+self.model)
        print("Starting a car with the color"+self.color)

lambo= Car("Lamborgini", "2024","Top End", "White")
print("=========================")
lambo.start_engine()
print("=========================")

mahi = Car("Mahendra XUV", "2025", "Higher end", "Black")
print("=========================")

print("=========================")
mahi.start_engine()


