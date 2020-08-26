#Find the max length of subarray which has non negative elements.

def nonnegativesubarray(list1):
    list2 = []
    max1 = 0
    for i in range(len(list1)):
        count1 = 0
        for j in range(i,len(list1)):
            if(list1[j]>=0):
                count1+=1
            else:
                break
        list2.append(count1)
    
    for k in range(len(list2)):
        if(list2[k]>max1):
            max1 = list2[k]
    return (max1)
#nonnegativesubarray([1,2,5,-7,2,3,2,2,2,-3,-2,4,5,77,3,2,5,6,6])
print(nonnegativesubarray([-2,1,-2]))
            
