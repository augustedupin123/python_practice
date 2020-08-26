#Rotate list A with B positions

'''def listrotate(list1,k):
    list3 = []
    for i in reversed(range(1,k+1)):
        list3.append(list1[-i])
    for j in range(len(list1) - k):
        list3.append(list1[j])
    return(list3)
print(listrotate([11,12,13,14,15,16],3))'''


def rotate(list1,k):
    list2 = []
    q = len(list1)
    s = len(list1) - k
    for i in range(s,q):
        list2.append(list1[i])
    for j in range(s):
        list2.append(list1[j])
    return(list2)
print(rotate([11,12,13,14,15,16],-1))

    
