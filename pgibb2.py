#Program to remove an element from set if it is already present

def removeit(list1,num):
    a = set(list1)
    for i in a:
        if(i==num):
            a.remove(num)
    print (a)
b = int(input('hgdckfiljlb'))
removeit([2,3,4,5],b)


    
