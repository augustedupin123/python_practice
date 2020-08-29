#Given an unsorted array of size N. Find the first element in array such that
#all its left elements are smaller and all right elements are greater than it.

def left_to_right(list1):
    list2 = []
    for i in range(len(list1)):
        flag = 0
        for j in range(0,i):
            if(list1[j]>list1[i]):
                flag = 1
#                print(list1[i])
        for k in range(i,len(list1)):
            if(list1[k]<list1[i]):
                flag = 1
                
        if(flag==0):
            list2.append(list1[i])
    if(list1[-1]==list2[-1]):
        list2.remove(list1[-1])
    if(len(list2)==0):
        return('no such element')
    else:
        return(list2)
    
    
#            return(list1[i])
#        if(flag==1):
#            return('no such element')
print(left_to_right([10,9,11]))
