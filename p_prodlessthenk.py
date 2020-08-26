def prodless(list1,v):
    i = 0
    list2 = []
    count = 1
    while(i<len(list1)):
        while(count<v):
            count*=list1[i]
            i+=1
            
        i+=1
    print(list2)
prodless([1,2,3,4],14)

            
        

        
        

