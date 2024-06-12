# i=0
# while i < 5:
#     print(i)
#     i += 1
# year = int(input("Enter your year \n"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(" Yes Its a Leap Year :", year)
# else:
#     print("Its not a leap year putta", year)
year = int(input("Enter your year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes, it is a leap year:", year)
        else:
            print("It is not a leap year:", year)
    else:
        print("Yes, it is a leap year:", year)
else:
    print("It is not a leap year:", year)
