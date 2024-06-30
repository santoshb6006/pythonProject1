#SET
#1. Write a Python program to create a set.
sets = {1, 2, 3, 4, 5}
print(sets)
sets.copy()
print(sets)
# list of URL for API testing
envi_var_urls=tuple[("abc.com/get", "normal.com/post","higgaf.com/put")]
print(envi_var_urls)
for i in envi_var_urls:
    print(i)
#Tuples used for non-chenging and immutable data
#Sets used for chenging and mutable data
#2. Write a Python program to add an element to a set.
sets.add(6)