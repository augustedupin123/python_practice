#Write a program to print if a list is empty or not

def ifempty(list1):
    for i in list1:
        if (len(list1) == 0):
            return 0
        else:
            return 1
a = input('enter the list')
print (ifempty(a))