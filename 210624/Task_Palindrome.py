# # WAP for to check palindrome of the given string4
# def isPalindrome(s):
#     return s == s[::-1]
# s = "racecar"
# ans = isPalindrome(s)
# if ans:
#     print("Yes")
#     print("The given string is palindrome")
#
# print("========================================")
# #Palidrome code without in-build func()
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
strings =str(input("Enter the strigs to check:\n"))
print(isPalindrome(strings))

