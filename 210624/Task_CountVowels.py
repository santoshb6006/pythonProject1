# WAP to count the vowels in a given string by the user.

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


string = str(input("Enter the string:\n"))
vowels = count_vowels(string)
print(vowels)
