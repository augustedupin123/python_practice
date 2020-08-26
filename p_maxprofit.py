#Maxprofit geeksforgeeks.

'''def maxprofit(list1):
    list2 = []
    i = 0
    while(i<len(list1)):
        for j in range(i+1,len(list1)):
            list2.append(list1[j] - list1[i])
            
        i+=1
    print(list2)
maxprofit([100,180,260,310,40,535,695])'''


def maxprofit(list1):
    list2 = []
    i = 0
    
    while(i<len(list1)):
        for j in range(i+1,len(list1)):
            list2.append(list1[j] - list1[i])
            
        i+=1
    max1 = list2[0]
    for l in range(len(list2)):
        if(list2[l]>max1):
            max1 = list2[l]
    p = 0
    while(p<len(list1)):
        for q in range(p+1,len(list1)):
            if((list1[q] - list1[p]) == max1):
                print (p)
                print (q)
                break
        p+=1
            

    
maxprofit([100,-300,500,700,90,10,20])
