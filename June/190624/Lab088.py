list=[1,2,3,4,5,6,7,8,9]
print(list*2) # It prints the list twice
print(list+list) # It prints the list twice
print("========ONE============")
temp_list=[]
print(temp_list)
for g in list:
    temp_list=temp_list+[g*2]
    print(temp_list)
print("==========ONE END===================")
print(temp_list)
print("==========TWO===================")
list2=[10,11,12,13,14,15]
temp_list2=[]
for i in list2:
    temp_list2.append(i*2)
print(temp_list2)
print("==========TWO END===================")
print("==========THREE===================")
