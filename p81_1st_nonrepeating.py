#Write a program to find the first non repeating character in a given string

'''def string_nonrepeat(str1):
    str2 = ''
    for i in range(len(str1)):
        if (str1[i] not in str1[:i] and str1[i] not in str1[i+1:]):
            print (str1[i])
string_nonrepeat('abcaaxbxxklm')   

Above code is printing all unique chars'''

def func(str1):
    for i in range(len(str1)):
        if (str1[i] not in str1[:i] and str1[i] not in str1[i+1:]):
            print (str1[i])
            break
func('abcaaxxbxxklm')