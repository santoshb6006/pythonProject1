#Operators
#Arithmetic (+,-,/,*)
#Assignment (=)
#Augmented Assignment (+=, -=, /=, *=)
#Comparison (==, !=, >, <, >=, <=)
#Logical (and, or, not)
#Identity (is, is not)
#Membership (in, not in)
#Bitwise (&, |, ^, ~, <<, >>)

#Arithmetic
num =int(input("Num\n"))
num1=int(input("Num1\n"))
res=num+num1
print(res)
res=num-num1
print(res)
res=num*num1
print(res)
res=num/num1
print(res)

#Assignment
a=10
print(a)

#Comparison
Santosh=10
if Santosh == 10:
    print("Yes, Its ten")

#Arithmetic
print(10+3)

#unery Operator
a=+10
print(a)
b=-10
print(b)

age=65
num=-78
print(age)
print(num)
resu=(age-num) #BODMAS
print(resu)
print(resu)

#Not Operator
is_Married=False
print(is_Married)# works with only booleans

#is operator is mostly used in the list
a=10
b=89
print(a is b)
print(a is not b)

my_list=[1,2,3,4,5,6,7,8,9]
my_list1=[5,6,6,8,4,8,3,7,6,8,4]

print(my_list is my_list1)