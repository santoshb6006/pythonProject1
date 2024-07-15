letters_list=['a', 'e','i', 'o','u','k','l','r']
letters_tuple=('a', 'e','i', 'o','u','k','l','r')
letters_set={'a', 'e','i', 'o','u','k','l','r'}
print(letters_list,"I'm a list")
print(letters_set,"I'm a set")
print(letters_tuple,"I'm a tuple")
print("====================================")

def filter_vowels(letter_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter_list in vowels

def filter_vowels(letter_set):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter_set in vowels
def filer_vowels(letter_tuple):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter_tuple in vowels


filtered_vowels_list=filter(filter_vowels,letters_list)
print(list(filtered_vowels_list))
print("==========List Completed....Set started==========================")

filtered_vowels_set=filter(filter_vowels,letters_set)
print(list(filtered_vowels_set))
print("==========Set Completed....tuple started==========================")

filtered_vowels_tuple=filter(filter_vowels,letters_tuple)
print(list(filtered_vowels_tuple))
print("==========The END==========================")



print("============YES!! I'M A SECOND METHOD========================")

letters1=['a', 'e','i', 'o','u','k','l','r']
print(letters1)
def fileru_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letters1 in vowels:
        return True
    else:
        return False
filter_vowels=filter(fileru_vowels,letters1)
