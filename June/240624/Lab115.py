num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_me(n):
    return n * 2


doub_num = map(double_me,num)
print(list(doub_num))

doub_nu=map(lambda n:n*2, num)
print(list(doub_nu))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_giver(num):
    return num%2==0


new_list=filter(even_giver, num)
print(list(new_list))
new_lis=filter(lambda n:n%2==0, num)
print(list(new_lis))
new_lis=filter(lambda d:d%2==0,num)
print(list(new_lis))
print(list(filter(lambda u:u%2==0,num)))