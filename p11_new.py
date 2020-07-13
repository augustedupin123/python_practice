'''for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print()'''


'''for i in range(1,6):
    for j in range(1,6):
        print(j, end="")'''
    
'''for i in range(1,6):
    for j in range(1,6):
        print(j)'''

'''for i in range(1,6):
    print(str(i)*5)'''


'''for i in range(1,6):
    print((i)*5)'''


'''for i in range(65,70):
    for j in range(65,70):
        print(chr(i), sep="", end="")
    print()'''

'''for i in range(65,70):
    for j in range(65,70):
        print(chr(i), end="")
    print()'''

'''j = 5
while(j>0 and j<=5):
    i = 5
    while(i>0 and i<=5):
        print(i, end="")
        
        i -=1
    j-=1
    print()'''


'''for i in range(1,6):
    for j in range(0, 5-i):
        print(' ', end= "")
    for j in range(1, i+1):
        print(j, end="")
    print()'''

def sec_lar(list1):
    max1 = 0
    max2 = 0
    list2 = []
    for i in range(len(list1)):
        if(max1<list1[i]):
            max1 = list1[i]
    for j in range(len(list1)):
        if(list1[j]!=max1):
            list2.append(list1[j])
    for k in range(len(list2)):
        if(list2[k]>max2):
            max2 = list2[k]
    return (max2)
a = sec_lar([23,1244,235,23,423,34,23,235,23])
print (a)
    







    
