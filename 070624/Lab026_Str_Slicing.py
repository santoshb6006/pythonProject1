string="This is my string going to slice it"
print(string)
print(len(string))
print(string[0:5])
print(string[0:6])
print(string[6:15])
print(string[0:7:35])

#Reverse a string slice
print(string[13:-1])
print(string[35:-4])

#Partial Slicing
my_string="Hello World I love you"
print(my_string[0:10])
print(my_string[9:])
print(my_string[:])
print(my_string[::-1])
print(my_string[::2])
print(my_string[::3])

