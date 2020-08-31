#Given an array, find maximum (j-i) such that a[j]>a[i]

def array_problem(list1):
    list2 = []
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            if(list1[j]>list1[i]):
                list2.append(j-i)
    return max(list2)
if __name__=="__main__":
    print(array_problem([1,2,3,4,5,6]))
    
        
