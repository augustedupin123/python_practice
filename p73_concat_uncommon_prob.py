#Write a program to create a string from two given strings concatenating uncommon characters

'''def string_concatenate(str1, str2):
    str3 = ''
    for i in str1:
        for j in str2:
            if(j!=i):
                str3+=j
    print (str3)
a = input('enter str1')
b = input('enter str2')
string_concatenate(a,b)'''

def string_concatenate(str1,str2):
    str3 = ''
    str4 = ''
    for i in str1:
        if(i not in str2):
            str3+=i
    for j in str2:
        if(j not in str1):
            str3+=j
    for k in range(len(str3)):
        if (str3[k] not in str3[k+1:]):
            str4+=str(str3[k])

        
            
    print (str4)
a = input('enter str1')
b = input('enter str2')
string_concatenate(a,b)

