my_num = [1, 2, 3, 12, 4, 5, 6, 7, 8, 9]
letters=[]

def is_even_num(my_num):
    return my_num % 2 == 0
    print("Even numbers are:\n")


def is_lesser_than(my_num):
    return my_num <5

even_num = filter(is_even_num, my_num)
print(list(even_num))

lesser_num= filter(is_lesser_than,my_num)
print(list(lesser_num))

