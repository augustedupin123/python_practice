#Write a program to split a given list in two parts where the length of the first part is given

'''def split_lists(list1,n):
    print(list1[:n],list1[n:])
split_lists([243234,'fdfg',44,44,1244,1244,1244,2144,23123],5)'''


def split_lists(list1,n):
    return (list1[:n],list1[n:])
print (split_lists([243234,'fdfg',44,44,1244,1244,1244,2144,23123],5))
