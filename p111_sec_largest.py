#Second largest from a list

def sec_lar(list1):
    max1 = 0
    max2 = 0
    list2 = []
    for i in range(len(list1)):
        if(max1<list1[i]):
            max1 = list1[i]
    for j in range(len(list1)):
        if(list1[j]!=max1):
            list2.append(list1[j])
    for k in range(len(list2)):
        if(list2[k]>max2):
            max2 = list2[k]
    return (max2)
a = sec_lar([23,1244,235,23,423,34,23,235,23])
print (a)
