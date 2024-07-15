class A():
    def method_a(self):
        return "A methods"
class B(A):
    def method_b(self):
        return "B method"
class C(A):
    def method_c(self):
        return "C Methods"

class D(B,C):
    def method_B_C(self):
        return ""
    def multiple_return(self):
        return "AAPLEE", "9999", True

child=D()
print(child.method_b())
print(child.method_a())
print(child.method_B_C())
print(child.method_b())
print(child.multiple_return())
print(child.method_a())
print(child.method_b())
print(child.method_a())

