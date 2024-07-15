my_list=[1,2,3,4,5,6,7,8,9,10]
def double_item(num):
        return num*2

double_list=list(map(double_item,my_list))
double_list1=lambda num:num*2, my_list
print(double_list)
print(double_list1)

print("Addition")
#addition of the list
add_list=[1,2,3,4,5]
def addition(num):
    return num+2
addd_list=list(map(addition,add_list))
print(addd_list)
print("Addition using lambda")
addd_list1=list(map(lambda num:num+2, add_list))

print(addd_list1)