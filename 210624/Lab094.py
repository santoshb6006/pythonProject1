my_tuple=("Apple", "Banana", "Cherry")
print(my_tuple)
print(my_tuple[0])# printing the 0th tuple
print(my_tuple[-1])# printing the last tuple# print(my_tuple[2])
print(my_tuple[1:4])# slicing the tuple
#my_list=list[my_tuple]# It will retuen the [('Apple', 'Banana', 'Cherry')]
my_list=list(my_tuple)
print(my_list)
my_list.append("Orange")
print(my_list)
my_list.insert(1,"Sapota")
print(my_list)
my_tuple=tuple(my_list)
print(my_tuple)