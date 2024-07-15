my_num = [1, 2, 3, 12, 4, 5, 6, 7, 8, 9]

def double_me (n):
    return n*2


double_num=map(double_me,my_num)
print(list(double_num))

# double_me_lambda=map(lambda n:n*2,my_num)
# print(list(double_me_lambda))
print(list(map(lambda n:n*2,my_num)))
