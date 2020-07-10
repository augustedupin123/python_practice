#Python: Get a single string from two given strings, separated by a space and swap the first two characters of each string
'''a = '@fmvinght'
print (a[1:2])
print (a[0:1])
print (a[0])'''

'''def combine_string(str1, str2):
    temp = 0
    a = str1[0]
    b = str2[0]
    temp = a
    a = b
    b = temp
    str3 = a + str1[1:] + " " + b + str2[1:]
    return str3
a = input('enter string 1')
b = input('enter string 2')
s = combine_string(a,b)
print(s)'''


def combine_string(str1, str2):
    temp = 0
    a = str1[0:2]
    b = str2[0:2]
    temp = a
    a = b
    b = temp
    str3 = a + str1[2:] + " " + b + str2[2:]
    return str3
a = input('enter string 1')
b = input('enter string 2')
s = combine_string(a,b)
print(s)
