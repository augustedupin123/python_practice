#Write a program to check if a string has all characters of the alphabet
'''def func(a):
    flag = 0
    c = ''
    b = 'abcdefghijklmnopqrstuvwxyz'
    for char in a:
        if char in b:
            c += char

    for char1 in b:
        if char1 not in c:
            flag = 1
    return flag
            
        
            
print (func('bmmhdy'))'''

def func(a):
    b = 'abcdefghijklmnopqrstuvwxyz'
    for i in b:
        if i not in a:
            print('No')
        else:
            print('yes')
print (func('the quick brown fox jumps over the lazy dog'))
