#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

def make_string(str1):
    if(len(str1) > 2):
        str2 = str1[0:2] + str1[-2:]
        return str2
    else:
        return str1
a = input('enter the string:')
y = make_string(a)
print (y)

    