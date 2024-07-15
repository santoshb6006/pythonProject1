# Filter in python
def filter_list(input_list):
    """
    This function takes a list as input and returns a new list containing only the integers from the original list.
    """
my_num_list=[1,2,3,4,5,6,7,8,9,10,12,13]
print(my_num_list)

def is_even(my_num):
    return my_num%2==0
filer_even=filter(is_even,my_num_list)
print(list(filer_even),":->All are even numbers")

def is_odd(n):
    return n%2!=0

filter_odd=filter(is_odd, my_num_list)
print(list(filter_odd),":->All are odd numbers")