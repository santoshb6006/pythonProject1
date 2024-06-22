# Multiple Cnditions
a = 100000
b = 20
x = 50
y = 200
result = (a > b)
result2 = (x < y)
result3 = (a > b and x < y)  # True and True = True #
print(result3)
result4 = result and result2
print(result4)

for i in range(1,11):
    print("Hello===>", i)