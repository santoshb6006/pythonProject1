#Functions Scope
var1 = 60 #Global variable

def func1():
    var2 = 10 #Local variable
    print("Var2 from func1", var2)
def outer_function():
    var1 = 20
    print("Var1 from outer function", var1)
    def inner_function():
        var2=80
        print("Var1 from inner function", var2)


    inner_function()

outer_function()

def outer_function():
    vari = 78
    print("I'm outer function variable:", vari)

    def inner_function():
        vari = 87
        print("I'm inner function variable:", vari)

    inner_function()


outer_function()
