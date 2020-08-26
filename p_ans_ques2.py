#Remove element with least frequency from list

def modifylist(list1):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        if(list1[i] not in list1[i+1:]):
            list2.append(list1[i])
    print(list2)
    for j in list2:
        count = 0
        for k in list1:
            if(k==j):
                count+=1
        list3.append(count)
    print(list3)
    min1 = min(list3)
    print(min1)
    
    x = 0
    for m in list2:
        count1 = 0
        for p in list1:
            if(p==m):
                count1+=1
        if(count1==min1):
            x = p
    print(x)

    for s in list1:
        if(s==x):
            del s
    return(list1)
print(modifylist([2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5]))
                  


    
    