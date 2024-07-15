
def sum_of_digits(num):
    sum_digits= 0
    while num>0:
        sum_digits+=num%10 # sum digits= sum digits + n%10
        num=num//10
    return sum_digits


print(sum_of_digits(1234567789))