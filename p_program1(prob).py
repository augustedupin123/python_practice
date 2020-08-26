#Max count of pairs which generate the same sum

def countpair(list1):
    list2 = []
    list3 = []
    
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            m = list1[i] + list1[j]
            list2.append(m)
    print(list2)
    print(set([l for l in list2 if list2.count(l)>1]))
countpair([1,2,3,4,6,5])

    