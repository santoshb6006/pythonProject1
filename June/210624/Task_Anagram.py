# # WAP to find the anamgrams
# def find_anagrams(s1, s2):
#     # Convert strings to lowercase and sort their characters
#     s1 = ''.join(sorted(s1.lower()))
#     s2 = ''.join(sorted(s2.lower()))
#
#     # Check if the sorted strings are equal
#     return s1 == s2
# # Example usage
# string1 = "listen"
# string2 = "silent"
# if find_anagrams(string1, string2):
#
#     print("The two strings are anagrams.")
# print("=================================================")

def check_anagram(s1,s2):
    if(sorted(s1)== sorted(s2)):
         print("The strings are anagrams.")
        # return True
    else:
        print("The strings are not anagrams.")
        # return False


s1="dad"
s2="add"

check_anagram(s1, s2)
# if check_anagram(s1,s2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")