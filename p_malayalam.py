'''def malayalam(str1):
    left = 0
    right = len(str1) - 1
    while(left<=right):
        if(str1[left]!=str1[right]):
            return False
        left = left +1
        right = right - 1
    return True
print(malayalam('refermadam'))'''

'''def malayalam(str1):
    a = 0
    b = len(str1) - 1
    while(b!=0):
        left = a
        right = b
        while(left<=right):
            if(str1[left]!=str1[right]):
                print ('False')
            left = left + 1
            right = right - 1
        print ('True')
    b = b - 1
print(malayalam('refermadam'))'''

'''def func(str1):
    a = 0
    b = len(str1) - 1
    while(b>0):
        left = a
        right = b
        while(left<=right):
            if(str1[left]==str1[right]):
                print('true')'''
'''def function5(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            for k in range(i,j):
                print(list1[k])
function5([122,2234,3,4])'''

'''def funct(str1):
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            for k in range(i,j+1):
                print(str1[k],end="")
            print()
funct('stdfg')'''



'''def sublist(list1):
    moura = [[]]
    for i in range(len(list1) + 1):
        for j in range(i+1,len(list1) + 1):
            list2 = list1[i:j]
            moura.append(list2)
    print(moura)
sublist([1,2,3,4,5])'''


'''def sublist(list1):
    moura = [[]]
    list3 = []
    for i in range(len(list1) + 1):
        for j in range(i+1,len(list1) + 1):
            list2 = list1[i:j]
            moura.append(list2)
    for k in moura:
        a = len(k)
        list3.append(a)
    for l in range(len(list3)):
        for m in range(l+1,list3)):
            for n in range(m+1,len(list3)):
                if()

    
sublist([1,2,3,4,5])'''
#the correct way for getting list of all sublists
'''list1 = [1,2,3,4,5]
list2 = []
for i in range(len(list1)):
    for j in range(len(list1),i,-1):
        list2.append(list1[i:j])
print(list2)'''

str1 = 'aaa'
y = len(str1)
list1 = []
list2 = []
for i in range(len(str1)):
    for j in range(len(str1),i,-1):
        list1.append(str1[i:j])
#print(list1)
for l in range(len(list1)):
    k = list1[l]
    if(k==k[::-1]):
        list2.append(k)
#print(list2)


for s in range(len(list2)):
    for t in range(s+1,len(list2)):
        if(list2[t] not in list2[s]):
            for w in range(t+1,len(list2)):
                if(list2[w] not in list2[t]):
                    if((len(list2[s])+len(list2[t])+len(list2[w])== y)):
                        if((list2[s]+list2[t]+list2[w])==str1):
                            print(list2[s],list2[t],list2[w])
                        
                
                    

    
    
    
    
    
    
'''for m in list1[l]:
        if(m==m[::-1]):
            list2.append(m)
print(list2)'''






                

            



        

        