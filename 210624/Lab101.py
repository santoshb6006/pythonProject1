set = {"The Santosh Academy", "For", "Danger ."}
print(len(set))
for i in set:
    print(i)
print("================")

# my_sets= set(["The Santosh", "For", "Dingi."])
#
# print(len(my_sets))
#
# for i in set:
#     print(i)

# my_set = set(["The Santosh Academy", "For", "Danger ."])
#
# print(len(my_set))
#
# for item in my_set:
#     print(item)


set1 = {1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12}

print(len(set1))
set1.pop()
print(set1)
set1.copy()
print(set1)
set1.clear()
print(set1)
set1.add(10)
print(set1)
set1.discard(10)
print(set1)
# set1.remove(2)
print(set1)
set1.update({10, 11, 12})
print(set1)
set1.intersection_update({10, 11, 12})
print(set1)
set1.difference_update({10, 11, 12})
print(set1)

