def checklastchar(x,h):
    flag = 1
    for i in range(len(x)):
        if(x[-1] == h):
            flag = 1
        else:
            flag = 0
    if(flag == 1):
        print('character entered is correct')
    if(flag == 0):
        print('character enter is wrong')
a = input('enter the string')
b = input('enter the character')
checklastchar(a,b)
