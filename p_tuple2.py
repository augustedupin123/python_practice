#Write python program to replace last values of tuples in a list.

def replacetuples(list1):
    for i in list1:
        if i is tuple:
            p = list(i)
            p[-1] = 100
            i = tuple(p)
            list1.append(i)
    print(list1)
replacetuples([2,3,(10,20,2,),4,(12,234,19,)])

'''def epalcetuple(list1):
    list2 = []
    list3 = []
    for i in list1:
        if i is tuple:
            list1.remove(i)
            list2.append(i)
    for j in list2:
        for k in list2[j]:
            list2[j][k][-1] = 100
    print(list2)
epalcetuple([2,3,(10,20,2),4,(12,234,19)])
wrong output'''


        

            
