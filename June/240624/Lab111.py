my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)
found = False
key = str(input("Enter the key to search\n"))
for k, v in my_dict.items():
    if k == key:
        print("Entered Key is found", key)
        found= True
        break
if not found:
        print("Entered Key is not found", key)

