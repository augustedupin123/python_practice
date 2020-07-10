#Write a program to remove the characters which have odd index values
#of a given string

def remove_odd_characters(str1):
    str2 = ""
    for i in range(len(str1)):
        if(i%2 == 0):
            str2 += str(str1[i])
    print(str2)
a = input('enter the value of the string:')
remove_odd_characters(a)