#Write a program to count number of sub strings with the same first 
#and last characters of a given string

'''def getsubstrings(str1,str2):
    
    p = str2[0]
    b = str2[len(str2) - 1]
    s = len(str2)
    count = 0
    for i in range(len(str1)):
        if(str1[i]==p and str1[i+s]==b):
            count+=1
    print (count)
a = input('enter str1')
b = input('enter str2')'''

def getsubstring(st1,st2):
    p = st2[0]
    b = st2[len(st2)-1]
    count = 0
    for i in range(len(st1)):
        if(st1[i]==p):
            if(b in st1[i+1:]):
                count+=1
    print (count)
a = input('enter string 1')
b = input('enter string 2')
getsubstring(a,b)
    

