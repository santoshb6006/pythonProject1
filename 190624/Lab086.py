#List/ collection of items
my_list = [3,2,1,4,5]
my_list2=[10,20,30,46,1,2,3]
print(my_list)
my_list.sort()
my_list.append(466)
print(my_list)
print(my_list2)
my_list.insert(3, 999)
full=my_list.__add__(my_list2)
print(full)
my_list.remove(999)
full=my_list.__add__(my_list2)
print(full)
my_list1=my_list.copy()
print(my_list1)
my_list1.extend(my_list2)
my_list2.reverse()# Reverse order
print(my_list2)
print(my_list1)
print("Clear")
my_list.clear()
print(my_list)
