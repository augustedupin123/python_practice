#Write a program to find the index of a given string at which a substing starts.

def index_string(str1,str2):
    n = len(str2)
    for i in range(len(str1)):
        if(str1[i]==str2[0] and str1[i:i+n]==str2):
            print (i)
        else:
            print ('not found')
a = input('enter the string')
b = input('enter sub string')
index_string(a,b)
            









'''a = 'ghtyloune'
print (a[8])'''





