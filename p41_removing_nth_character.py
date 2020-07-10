#Removing nth character from a non empty string.

'''def function1(str1):
    for i in str1:
        print (i)
a = input('string:')
function1(a)'''
'''output
b
o
l
t
o
n
'''

'''def function1(str1):
    for i in len(str1):
        print (i)
a = input('string:')
function1(a)
output: error'''

'''def function1(str1):
    for i in range(len(str1)):
        print (i)
a = input('string')
function1(a)
inputgiven: bolton
output:0
1
2
3
4
5
'''
'''def function1(str1):
    for i in range(len(str1)):
        print (str1)
a = input('string:')
function1(a)
input: bolton
output:
bolton
bolton
bolton
bolton
bolton
bolton
'''

'''def function1(str1):
    for i in range(len(str1)):
        if(str1[i] == 'n'):
            print(i)
a = input('string')
function1(a)
#showing position correctly
'''

'''def function1(str1):
    for i in range(len(str1)):
        print(str1[i])
a = input('string')
function1(a)'''

def remove_character(str1, n):
    str2 = ""
    for i in range(len(str1)):
        if(i!=n-1):
            str2 += str(str1[i])
    print(str2)
num1 = int(input('enter n:'))
str3 = input('string:')
remove_character(str3, num1)

        


