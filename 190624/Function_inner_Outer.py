var1=60
def outer_function():
    var1 = 20
    def inner_function():
        var2=80
        print("Var1 from outer function", var1)


    inner_function()

print(outer_function())
