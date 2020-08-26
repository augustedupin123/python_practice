def longest_common(str1,str2):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for i in range(len(str1)):
        for j in range(len(str1),i,-1):
            list1.append(str1[i:j])
    for k in range(len(str2)):
        for l in range(len(str2),k,-1):
            list2.append(str2[k:l])
    for m in list2:
        if m in list1:
            list3.append(m)
#    print(list3)
    for p in range(len(list3)):
        list4.append(len(list3[p]))
    print(max(list4))
        
    
    
longest_common('geeksabcxyxvtygeek','geeksquizabcxyxvty')
