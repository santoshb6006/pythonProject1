#List
# A list in the python is  a collection of items in a particular order which can be of same types or different types.
# The items in the list are separated by commas and enclosed within square brackets.
# The items in the list are indexed starting from 0.
# The list can be empty.
# The list can contain duplicate items.
# The list is mutable.

my_list = [1, 2, 3, 4, "Hello", 'Hi', 5.0, "Hello"]
print(my_list)

#Deleting, updating and sorting of a list
print(len(my_list))
del my_list[7]
print(my_list)
my_list.append("Milk")
print(my_list)
my_list.extend(["Pedha", "Gajar", "Kunda"])
print(my_list)
#print(sorted(my_list))# TypeError: '<' not supported between instances of 'str' and 'int'


