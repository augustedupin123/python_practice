#Write a python program to find the first repeated character in a given string.

def first_repeated(str1):
    for i in range(len(str1)):
        if(str1[i] in str1[:i] or str1[i] in str1[i+1:]):
            print(str1[i])
            break
first_repeated('abcdefghbbhutanxdkfn')