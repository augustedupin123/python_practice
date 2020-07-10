#Write a program to pack consecutive duplicate elements into sublists.

def packconsecutive(list1):
    list2 = []
    list3 = []
    for i in range(len(list1) - 1):
        if(list1[i]==list1[i+1]):
            list2.append([list1[i],list1[i+1]])
    for s in range(len(list1) - 1):
        if(list1[s]!=list1[s+1]):
            list3.append(list1[s])
    print (list2 + list3)
packconsecutive([1,2,3,4,4,6,7,8,9,10,10,19,25,30,30])
        
            

    