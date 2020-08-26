#Gen binay string without consecutive 0 and at most k consecutive
#1. n :no. of 0, m:no. of 1

'''def func(n,m,k):
    
    d = 0
    count = 0
    
    list1 = []
    while(d<n):
        list1.append(0)
        for l in list1:
            if(l==1):
                count+=1
        for j in range(k):
            if(count==m):
                break
            list1.append(1)
                
        d+=1
    print(count)
    print (list1)
func(4,18,4)'''
        
def func(n,m,k):
    
    d = 0

    list1 = []
    count = n*k - m
    if(count<0):
        w = m - (n*k)
        for x in range(w):
            list1.append(1)
    while(d<n):
        list1.append(0)
        
        for j in range(k):
            
            list1.append(1)
                
        d+=1
    print(list1)
    for i in reversed(range(len(list1))):
        del list1[i]
        if(len(list1)==n+m):
            break
    print (list1)
func(4,18,4)
        
        
        
        


        