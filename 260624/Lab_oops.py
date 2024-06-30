# oops concepts
#Object oriented programming language
#class - blueprint of an object
#object - instance of a class# Its a real world entity which will have the state/Attributes and behavior
#DRY - don't repeat yourself

class computer:
    def config(self):
        print("i5, 16gb, 1TB")
class car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_info(self):
        print("Car name:", self.name)
        print("Car model:", self.model)
        print("Car color:", self.color)