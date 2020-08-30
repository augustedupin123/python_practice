#Given an array of n integers arranged in a circular fashion.Find
#the maximum contigious subarray sum.
def rotation(list1):
    list2 = []
    list3 = []
    N = 1
    
    while(N!=len(list1)+1):
        for i in range(len(list1)-N,len(list1)):
            list2.append(list1[i])
        for j in range(len(list1)-N):
            list2.append(list1[j])
#        print(list2)
        list3.append(list2)
#        print(list3)
        list2 = []
        N+=1
#    print(list3)
    list4 = []
    for l in list3:
        for s in range(len(l)):
            for t in range(len(l),s,-1):
                sum1 = 0
                for k in l[s:t]:
                    sum1+=k
                list4.append(sum1)
    for m in list3:
        for n in range(len(m)):
            for q in range(len(m),n,-1):
                sum2 = 0
                for s1 in m[n:q]:
                    sum2+=s1
                if(sum2==max(list4)):
                    print(m[n:q])
                break
rotation([4,-2,3,2,-4,6])












