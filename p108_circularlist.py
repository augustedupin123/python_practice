#Circular list

def circular_list(list1,list2):
    list3 = []
    s = len(list1)
    m = list1[-1]
    list3.append(m)
    
    for i in range(len(list1) - 1):
        
        list3.append(list1[i])
    print (list3)
    if(list2==list3):
        print ('circular')
    else:
        print ('not circular')
circular_list([10,10,2,0,10],[10,10,10,0,0])



'''def circular_list(list1,list2):
    list3 = []
    s = len(list1)
    
    list3[0] = list1[-1]
    
    for i in range(len(list1) - 1):
        
        list3.append(list1[i])
    print (list3)
    if(list2==list3):
        print ('circular')
circular_list([10,10,0,0,10],[10,10,10,0,0])

#error reason'''

