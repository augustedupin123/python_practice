#Print a list after removing even numbers from it.

'''def func(list1):
    list2 = []
    for i in list1:
        if(i%2==0):
            list2.append(i)
    print (list2)
func([1,3,2,4,5,6,9,7])'''

#print index of a list

'''def index(list1):
    for i in range(len(list1)):
        print (i)
index([2,77777,132,5,6,7,8,9])'''

#Print index of an item in a specified list

'''def index_of_item(list1,n):
    for i in range(len(list1)):
        if(list1[i] == n):
            print (i)
index_of_item([2124, 1244, 423235, 98765], 1244)'''

#Append a list to the second list

'''def append_to_list(list1,list2):
    listfinal = list1 + list2
    print (listfinal)
append_to_list([23123, 24234, 2434234, 24235, 23235], [213123, 234234, 235235, 34235, 235235])'''

#Unique values from a list

'''def unique_from_list(list1):
    for i in range(len(list1)):
        if( list1[i] not in list1[i+1:]):
            print (list1[i])
unique_from_list([2,2,2,3,4,5,7,7,63])'''

#Count the no. of elements within a specified range

'''def count_elements(list1,min1,max1):
    count = 0
    for i in range(len(list1)):
        if list1[i]>=min1 and list1[i]<=max1:
            count+=1
    print (count)
count_elements([5001,4000,5003], 5000, 8384)'''







