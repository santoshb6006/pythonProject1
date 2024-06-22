# to find the max numbet among three numbers
def find_max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    print("max is c",c)

a=int(input("Enter Num a\n"))
b=int(input("Enter the num b\n"))
c=int(input("Enter the num c\n"))

print (find_max_num(a,b,c))