# Multiple condition of java
# Switch matches
number = int(input("Enter the number\n"))


match number:
    case 1:
        print("Case1")
        print("case 2 also")
    case 2:
        print("Case2")
    case 3:
        print("Default case")
