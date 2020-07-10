#Write a python program to cout the no. of vowels in a given text and dispplay them.

def count_vowels(str1):
    count = 0
    for i in range(len(str1)):
        if(str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u'):
            count+=1
            print (str1[i])
    print (count)
a = input('enter string')
count_vowels(a)


