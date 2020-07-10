#Write a program to split a list every nth element

def split_list(list1,num1):
    for i in range(num1):

        print (list1[i::num1])
split_list([1232,124234,124,12,1244,2,1244,12424,214,24,124,24124],2)
