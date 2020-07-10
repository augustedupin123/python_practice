#Write a program to print a string in upper and lower cases
'''a = 'A'
print (ord(a))'''

'''for i in range(100,120):
    print (chr(i))'''

'''for i in range(200,400):
    print(chr(i))'''

'''m = 'swrjryeraeryy'
for i in range(len(m)):
    print(ord(m[i]))'''

'''m = 'dngnsdigg'
for i in range(len(m)):'''

Str1=input("Enter the string to be changed: ")

for i in range(len(Str1)):
    x = ord(Str1[i])
    if x>=97 and x<=122:
        x = x - 32
    elif x>=65 and x<=90:
        x = x + 32
    print(chr(x))

'''y=chr(x)
print(y,end="")'''

'''def toUppercase(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in s:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i>=26:
            result += x
        else:
            result += alphabet[i+26]
    return result

print(toUppercase('aslidwurhguern934892u3'))'''

    
