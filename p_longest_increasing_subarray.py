#Find the length of longest increasing subarray in a given array.

def sfddih(list1):
    n = len(list1)
    list2 = []
    i = 0
    
    
    
    while(i<n):

        count = 1

        while(i<(n-1) and list1[i]<list1[i+1]):
            count+=1
            i+=1
        list2.append(count)
        i+=1
    max2 = list2[0]
    for j in range(len(list2)):
        if(list2[j]>max2):
            max2 = list2[j]
    return(max2)


print(sfddih([2,3]))

