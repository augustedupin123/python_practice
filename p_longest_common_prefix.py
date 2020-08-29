#Find the longest common prefix in an array of strings.
def a_o_s(list1):
    list2 = []    
    for i in range(len(list1)):
        j = 0
        for k in range(len(list1[i]),j,-1):
            s = list1[i][j:k]
            count = 0
            for t in range(len(list1)):
                if s in list1[t]:
                    count+=1
            if(count==len(list1)):
                list2.append(s)
    nbv = max(list2, key = len)
    print(nbv)
a_o_s(['abcgthy','abcgthuyedct'])

