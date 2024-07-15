t=("Santosh Bagali", "Madhu Patil")
print(t)
print(set(t))
print("++++++++++++++++++")

set1={78,79,80}
set2={80,81,82}
# my_set=set1.union(set2) # Or Operator
# print(my_set)
# print("Uninon")
# print(set1.union(set2))#Removes common items from both sets
# print(set2 |set1 )
# print("Union")
# ui= set1.union(set2)
# print(set1|set2)#Connects
inter=set1.intersection(set2) #prints only the common item AND Operator
print(inter)
print("Intersection")
inte =(set1 & set2)
print(inte)
print("Difference")
my_set=set2.difference(set1)
print(my_set)
my_set=set1.difference(set2)
print(my_set)