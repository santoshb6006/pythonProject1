# Method Overloading is not supported in the python

class Mathutils():
    def add(self, a, b=0, c=0):
        return a + b + c

    def add(self, a, b, c):
        return a + b + c


math = Mathutils()
print(math.add(2, 3, 5))
#print(math.add(a=1))
print(math.add(12, 8, 5))
