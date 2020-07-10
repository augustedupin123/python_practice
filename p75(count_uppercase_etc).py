#Write a program to count uppercase, lowercase numeric and special characters in a given string

'''i = "sdfsngndfh"
for j in i:
    print (ord(j))'''

def count_characters(str1):
    uppercase = ''
    lowercase = ''
    numeric = ''
    special_char = ''
    for j in str1:
        if (ord(j)>=33 and ord(j)<=47):
            special_char+=j
        elif (ord(j)>=48 and ord(j)<=57):
            numeric+=j
        elif (ord(j)>=65 and ord(j)<=90):
            uppercase+=j
        elif (ord(j)>=97 and ord(j)<=122):
            lowercase+=j 

    print (special_char)
    print (numeric)
    print (uppercase)
    print (lowercase)

a = input('enter string')
count_characters(a)


