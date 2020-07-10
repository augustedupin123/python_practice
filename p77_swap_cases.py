#Write a python program to swap cases of a given string in python

def swap_cases(str1):
    str2 = ''
    for i in str1:
        j = 0
        if(ord(i)>=65 and ord(i)<=90):
            j = ord(i) + 32
            str2+=chr(j)
        elif (ord(i)>=97 and ord(i)<=122):
            j = ord(i) - 32
            str2+=chr(j) 
    print (str2)
a = input('enter string')
swap_cases(a)

'''i = 's'
j = ord(i) - 32
print (chr(j))'''
            


