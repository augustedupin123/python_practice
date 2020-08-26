#Print the length of longest sub list of a list of non negative integers

def longest_sublist(list1):
    i = 0
    list4 = []
    while(i<len(list1)):
        count = 0
        while(i<=(len(list1) - 1) and list1[i]>0):
            count+=1
            i+=1
        list4.append(count)
        i+=1
    max1 = list4[0]
    for l in range(len(list4)):
        if(list4[l]>max1):
            max1 = list4[l]
    return(max1)
print(longest_sublist([-2,-3,1,2,3,4,-6,-7,23423,235,5,2355,235,235,235,25,2662626]))

    
