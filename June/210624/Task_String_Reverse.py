#WAP to reverse the string
def reverse_string(in_string):
    char_list = list(in_string)
    reversed_list = char_list[::-1]
    reversed_string=''.join(reversed_list)

    return reversed_string

in_string = str(input("Enter the string to be reversed:\n"))
reversed_string = reverse_string(in_string)
print("The reversed string is:",reversed_string)