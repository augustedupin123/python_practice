#Write a program to check whether a string starts with a special character.
def specialchar_strings(a,b):
    for char in a:
        if (char[0] == b):
            print('yes')
            break
        else:
            print('no')
x = input('enter the string')
y = input('enter the character')
specialchar_strings(x,y)