my_dict={'a':1,'z':2,'e':3,'f':4,'g':5,'i':6,'l':7,'n':8,'o':9,'p':10,'m':22}
print(my_dict)
print(sorted(my_dict.items()))
print(sorted(my_dict.items(), key=lambda x:x[1]))
print(dict(sorted(my_dict.items(), key=lambda x:x[1])))
print(dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True)))
my_dict['l']=100
my_dict['m']=900
my_dict['a']=80
print(my_dict)

for k,v in my_dict.items():
    print(k, v)