#Write a program to remove all consecutive duplicates from a given string
def remove_consecutive_duplicates(str1):
    str2 = ''
    for i in range(len(str1)-1):
        if(str1[i]!=str1[i+1]):
            str2+=str(str1[i])
    print (str2)
#    print str(len(str1) - 1)
a = remove_consecutive_duplicates('asdgabcxxxxvcammnnhuytastttdg')
#Print last element of the string

