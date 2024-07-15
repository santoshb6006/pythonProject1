num=[1,2,3,4,5,6,7,8,9,10,11,12,13]

def greater(num):
    return num>5

greater=filter(greater, num)
print(list(greater),":->Greater than 5")
