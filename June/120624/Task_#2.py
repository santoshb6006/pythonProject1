# Write a script to find the leap year
#2
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
