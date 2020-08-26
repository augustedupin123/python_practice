#Check whether two strings are isomorphic

def isomorphic(str1,str2):
    list1 = []
    list2 = []
    if(len(str1)!=len(str2)):
        return(0)
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if(str1[j]==str1[i]):
                list1.append(i)
                list1.append(j)

    for l in range(len(str2)):
        for m in range(l+1,len(str2)):
            if(str2[m]==str2[l]):
                list2.append(l)
                list2.append(m)
    if(list1==list2):
        return('yes')
    else:
        return('no')
print(isomorphic('aab','xxy'))

        
