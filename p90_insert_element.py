#Write a program to insert an element before each element in a list

def insert_element(list1):
    list2 = []
    a = 'a'
    for i in list1:
        list2.append(a)
        list2.append(i)
    print (list2)
insert_element(['red','green','sgddfhdfh','sgdfhdfh'])
