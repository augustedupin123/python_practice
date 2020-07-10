#Write a program to find the list of words that are longer than n from a given list of words

def func(list1,num1):
    list2 = []
    list3 = list1.split()
    for i in list3:
        if(len(i)>num1):
            list2.append(i)
    print (list2)

a = input('enter list elements')
b = int(input('num value?'))
func(a,b)