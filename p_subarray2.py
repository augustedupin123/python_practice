#Find the contiguos subarray which has the maximum sum.

'''def func(list1):
    list2 = []
    for i in range(len(list1)):
        sum1 = 0
        j = len(list1) - 1
        while(j>=i):

            sum1+=list1[j]
            if(j==i):
                break
            j-=1
        list2.append(sum1)
#        for j in reversed(range(len(list1),i)):
#            sum1+=list1[j]
#        list2.append(sum1)
    print(list2)
    max1 = list2[0]
    for l in list2:
        if(l>max1):
            max1 = l
    print(max1)
func([1,2,3,4,-10])'''

'''def func(list1):
    list2 = []
    for i in range(1,len(list1)):
        sum1 = 0
        j = len(list1) - 1
        while(j>(i-1) or j==0):
            k = j
            while(k>(i-1) or k==0):
                sum1+=list1[k]
            
            k=k-1
            list2.append(list1[k])
        j=j-1
            
        list2.append(sum1)

    print(list2)
    max1 = list2[0]
    for l in list2:
        if(l>max1):
            max1 = l
    print(max1)
func([1,2,3,4,-10])'''

def sumsubarray(list1):
    list2 = []
    n = len(list1)
    for i in range(n):
        for j in range(i,n):
            sum1 = 0
            for k in range(i,j+1):
                sum1+=list1[k]
            list2.append(sum1)
    print(list2)
    print(max(list2))
sumsubarray([2,-1,-2,10,5,100])




