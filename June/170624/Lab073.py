def make_pizza(*toppings):
    for i in toppings:
        # print(toppings)
        print(i)

#
#santosh= make_pizza("pepperoni","Paneer", "Extra cheese")# tupels
# make_pizza("chicken", "onion", "capsicum")# tupels
make_pizza=["chicken", "onion", "capsicum"]# list
make_pizza.append("Paneer")
print(make_pizza)
