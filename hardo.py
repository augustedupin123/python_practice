def program(list1):
    list2 = []
    for i in range(len(list1)):
        count = 0

        for j in range(len(list1)):
            if(j!=i):
                count+=list1[j]
                for k in range(j+1,len(list1)):
                    if(k!=i):
                        count+=list1[k]
                    list2.append(count)
    print(list2)
program([0,1,2,3])
                
                    
                




                


        