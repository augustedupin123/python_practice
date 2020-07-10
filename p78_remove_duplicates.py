#Write a program to remove duplicate characters from a string

def remove_duplicate(str1):
    str2 = ''
    for i in range(len(str1)):
        if(str1[i] not in str1[:i] and str1[i] not in str1[i+1:]):
            str2+=str(str1[i])
    print (str2)
a = input('enter string')
remove_duplicate(a)
        
            