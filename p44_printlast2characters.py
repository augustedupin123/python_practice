#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
def string_copies1(str1):
    characters = str1[-2:]
    for i in range(1,5):
        print (characters, end="")
a = input('enter characters')
string_copies1(a)








'''def string_copies(str1):
    characters = str1[-2:]
    print (str(characters)*4)
a = input('string:')
string_copies(a)'''
