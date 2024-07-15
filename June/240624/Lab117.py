#LeetCode - Sum of Digits

num= int(input("Enter the num\n"))

def sum_of_digits(num):
   #Base case
    if num<10:
        return num
   #Recursive case
    else:
        return num%10 + sum_of_digits(num//10)
print(sum_of_digits(num))



# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10