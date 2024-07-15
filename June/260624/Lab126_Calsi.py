class Calc:
    def __init__(self):
        print("Hello Calci")
    def sum(self,a,b):
        return (a+b)

    def sub (self,a,b):
        return (a-b)

    def mul(self,a,b):
        return (a*b)
    def div(self,a,b):
        return (a/b)


calcu=Calc()
sum =calcu.sum(12,56)
print(sum)
print(calcu.sum(12,56))
print("==================")

sub=calcu.sub(12,56)
print(sub)
print("==================")
mul=calcu.mul(12,56)
print(mul)
print("==================")
div=calcu.div(12,56)
print(div)
print("==================")





