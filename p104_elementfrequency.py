#Write a program to remove kth element from list

'''def consecutive_duplicatelist(list1,k):
    list1.pop(5)
    print (list1)
a = input('enter values')

list1 = [83456893746,1242375,238423462735]

print ((list1))'''

#Write a program to print element frequency

def frequency(list1):
    list2 = []
    for i in range(len(list1)):
        if(list1[i]  not in list1[i+1:]):
            list2.append(list1[i])
    
    for i in list2:
        count = 0
        for j in list1:
            if(j==i):
                count+=1
        print ('count of')
        print (i)
        print('is')
        print (count)
            
    




frequency([2,2,1,3,9,1,3,2,0,3])
        
            


                        



