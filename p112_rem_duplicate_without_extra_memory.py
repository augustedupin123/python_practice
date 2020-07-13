def remove_duplicates(list1):
    for i in range(len(list1)):
        if (i==len(list1)):
            break

        if list1[i] in list1[i+1 : ]:
            del list1[i]
    return (list1)
print (remove_duplicates([22,1,33,3,8,8,9,9,3,3,4,4,22,33,2]))