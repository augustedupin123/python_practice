def arrays(list1):
    list2 = []
    for i in range(len(list1)):
        prod = 1
        j = 0
        for j in range(len(list1)):
            if(j!=i):
                prod = prod*list1[j]
        list2.append(prod)
    print(list2)
arrays([10,3,5,6,2])
     
        
