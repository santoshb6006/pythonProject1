def print_argument():
    print("Hello World")
print(print_argument())

def print_argument(*args):
    for i in args:
        print(i, end="\n")


print_argument("Santu", "Mantu", "Kantu")

my_list = ["santu", "Mantu", "Ghantu", "Chandu"]
for i in my_list:
    print(i)
