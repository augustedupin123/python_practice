"""def length1(x1, x2):
    print(len(x1))
    print(len(x2))
y1 = input('enter length1')
y2 = input('enter length2')
length1(y1, y2)"""

def comparestring(x1, x2):
    flag = 0
    if(len(x1)!=len(x2)):
        flag = 1
    for i in range(len(x1)):
        if(x1[i]!=x2[i]):
            flag = 1
            break
    if(flag == 1):
        print('not equal')
    else:
        print('equal')
A = input('enter first string')
B = input('enter second string')
comparestring(A, B)
