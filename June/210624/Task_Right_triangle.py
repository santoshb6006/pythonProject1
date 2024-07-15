#Right angle Tringle of stars
n=int(input("Enter the number of rows to be taken:"))
for n in range(n+1):
    print('*'*n)
print("===============================")
#Right angle Triangle of stars
rows=int(input("Enter the number of rows to be taken:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end="")
    print()
print("===============================")
rows =int(input("Enter the number of rows to be taken:"))
for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print('*', end="")
    print()
print("===============================")


