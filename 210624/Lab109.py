# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.6, dictionaries are ordered by default.
# Dictionaries are written with curly brackets, and have keys and values.

# Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "brand": "Ford" # Changing the brand name by overriding
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
print(thisdict.get("year"))
print(thisdict.keys())  # Get a list of the keys
print("======DICT1======")
thisdict1 = {"brand": "Mercedez", "model": "S class", "year": "2020"}
print(thisdict1)
print(thisdict1.values())  # Get a list of the values
print(thisdict1.keys())  # Get a list of the Keys
print(thisdict1.items())  # Get a list of the key-value pairs\
print(thisdict1)
print("USING FOR LOOPS")
for k,v in thisdict.items():
    print(k,v)

print("======DICT2 FOR LOOPS======")
for k,v in thisdict1.items():
    print(k, v)

