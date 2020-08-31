#Length of Longest subarray having sum of elements atmost K

def longsub(list1,K):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list1),i,-1):
            list2.append(list1[i:j])
    for s in range(len(list2)):
        w = 0
        for t in list2[s]:
            w+=t
        if w<=K:
            list3.append(list2[s])
    return(len(max(list3, key=len)))
if __name__ == "__main__":
    list1 = [1,2,1,0,1,1,0]
    print(longsub(list1,4))
    
    
    
    