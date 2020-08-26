def sublists(list1):
    list2 = []
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            for k in range(i,j):
                print(list1[k], end=" ")
            print("/n",end=" ")
sublists([2,4,5,6,3,1])


    

    