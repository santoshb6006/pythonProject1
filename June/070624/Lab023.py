#list - its a mutable data type
#list is a collection of data
#list is a ordered data type
# Add item to a list
# remove item from a list
#  update item in a list
#  access item in a list
#  iterate over a list\
#  list slicing #  list comprehension
shopping_list=["milk", "tea", "soap",  "toothpaste"]
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
shopping_list.append("rice")
print(shopping_list)
print(shopping_list[1])
print(shopping_list.remove("soap"))
print(shopping_list)
print(shopping_list.pop(1))
shopping_list.insert(5,"Apple")
print(shopping_list)
shopping_list.extend(["Bread", "Bread", "Chocolate"])
print(shopping_list)
print(shopping_list.count("Bread"))
print(shopping_list.sort())
print(shopping_list)
print(shopping_list.reverse())
print(shopping_list)
