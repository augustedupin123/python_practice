"""def checkfirstchar(x,h):
    flag = 1
    for i in range(len(x)):
        if(x[0] == h):
            flag = 1
        else:
            flag = 0
    if(flag == 0):
        print('wrong')
    else:
        print('right')
a = input('enter the string')
b = input('enter the character')
checkfirstchar(a,b)"""

def checkfirstchar(x,h):
    for i in range(len(x)):
        if(x[0] == h):
            return 1
        else:
            return 0
a = input('enter the string')
b = input('enter the character')
x = checkfirstchar(a,b)
print (x)