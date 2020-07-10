#Write a program to print the numbers of a specified list after removing
#even numbers from it

'''def remove_even(list1):
    list3 = []
    list2 = list1.split()
    for ele in list2:
        if(ele%2==0):
            list3.append(ele)
    print (list3)
a = input('enter the elements')
remove_even(a)'''

def func(list1):
    list3 = []
    list2 = list1.split()
    for i in list2:
        if(int(i)%2==0):
            list3.append(i)
    print (list3)
a = input('enter the values')
func(a)