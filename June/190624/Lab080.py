num=[1,2,3] #list-> Collection of the items

def do_something(santu):
    santu.append(4)# It's a local variable # Run-time
    # num.append(5)
    # num.pop()
    # print(num)
    # num[0]=10
    # num.extend([6,7])
    # num.sort()
    # num.reverse()
    return santu
l=do_something(num)
print(l)