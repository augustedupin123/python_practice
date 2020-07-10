#Write a program to find the list in a list of lists whose sum is the highest

def sum_lists(list1):
    list2 = []
    max1 = 0
    
    for i in range(len(list1)):
        sum_count = 0
        for j in list1[i]:
            sum_count+=j
        list2.append(sum_count)
    for k in list2:
        if(k>max1):
            max1 = k
    for i in range(len(list1)):
        sum1 = 0
        for q in list1[i]:
            sum1+=q
        if(sum1==max1):
            print (list1[i])

    
sum_lists([[1,2,3],[4,5,6],[234234,34234235,235235235]])




    
    
        



