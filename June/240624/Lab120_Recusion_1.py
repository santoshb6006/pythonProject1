#LeetCode Prg- Sum of Digits

num=123456

def recursive_case(num):
    if num<10:
        return  num
    #Recursive case
    else:
        return num%10 + recursive_case(num//10)



print(recursive_case(num))