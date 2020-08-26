#Write a program to remove an item fom a tuple

'''def removeitem(tuple1,m):
    l = 0
    for i in range(len(tuple1)):
        if(tuple1[i]==m):
            l = i
    tuplex = tuple1[:i] + tuple1[i+1:]
    list2 = list(tuplex)
    list2.remove(m)

    return(list2)
print(removeitem((2,4,5,6,7,8,92,3,3,3),(5)))'''

'''def removetuple(tuple1,m):
    list1 = list(tuple1)
    list1.remove(m)
    tuple2 = tuple(list1)
    return(tuple2)
print(removetuple(('2334','244','244','434','2535','23523','5','2235','32523','2335'),('434')))
correct output'''

def removetuple(tuple1,m):
    list1 = list(tuple1)
    list1.remove(m)
    tuple2 = tuple(list1)
    return(tuple2)
print(removetuple((2334,244,244,434,2535,23523,5,2235,32523,2335),(434)))


