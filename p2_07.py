#Write a program to find the 2nd largest element from a list

'''def second_largest(str1):
    list1 = str1.split()
    list2 = []
    max1 = 0
    for i in range(len(list1)):
        if(list1[i]>max1):
            max1 = list1[i]
    for j in range(len(list1)):
        if(list1[j]!=max1):
            list2.append(list1[j])
    print (list2)
a = input('enter string elements:')
second_largest(a)'''
     
def second_largest(list1):
    
    list2 = []
    max1 = 0
    for i in range(len(list1)):
        if(list1[i]>max1):
            max1 = list1[i]
    for j in range(len(list1)):
        if(list1[j]!=max1):
            list2.append(list1[j])
    print (list2)

second_largest([22, 35345, 1231244, 23255, 3535456, 23525262626])
