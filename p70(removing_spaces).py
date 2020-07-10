#Write a python program to remove spaces from a given string

def remove_spaces(str1):
    str2 = ''
    for i in range(len(str1)):
        if(str1[i]!= ' '):
            str2+=str(str1[i])
    print (str2)
a = input('enter string')
remove_spaces(a)


