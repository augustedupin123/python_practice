def nonoverlap(list1,K):
    count = 0
    
    for i in range(len(list1)):
        if(list1[i]==K):
            count4 = 0
            for j in range(K+1,len(list1)):
                if(list1[j]<=K):
                    count4+=1
                list2.append(count4)
                else:
                    continue
        else:
            continue
            
    for l in range(len(list1)):
        count = 0
        while(l<len(list1) and list1[l]<=k):
            count+=k
        
                    