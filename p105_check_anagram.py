#Write a program to check if two strings are anagrams of each other

def checkanagram(str1,str2):
    str3 = ''
    str4 = ''
    list1 = []
    bg = 0
    sa = 0
    for i in range(len(str1)):
        if(str1[i] not in str1[i+1:]):
            str3+=str1[i]
    for j in range(len(str2)):
        if(str2[j] not in str2[j+1:]):
            str4+=str2[j]
    for i in str3:
        
        
        for j in str1:
            if(j==i):
                bg+=1
        
    for l in str4:
        for m in str2:
            if(m==l):
                sa+=1
    
    if(bg==sa):
        print ('anagrams')
    else:
        print ('not anagrams')
    checkanagram('themorsecodeaergehh','herecomedots')
