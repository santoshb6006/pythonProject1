#Tuple its a collection which is ordered and unchangeable
#Its also a collection of items
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0]) #accessing the first element of the tuple
print(fruits[2])
#fruits[0] = "kiwi" #this will give an error because tuples are unchangeable
#fruits[1]=234
print(fruits)
#Tuple is immutable, but we can convert it into a list and then modify it
fr_list=list(fruits)
fr_list[2]="kiwi"
fr_list.append("orange")
fruits1=tuple(fr_list)
print(fruits1)
my=list(fruits)
print(my)
my.append("Mangoes")
my1=tuple(my)
print(my1)