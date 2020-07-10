#Print the string after a special character.

def string_special(a,b):
    for i in range(len(a)):
        if(a[i]==b):
            print(a[i:])
x = input('enter the full string')
y = input('enter the special character')
string_special(x,y)   