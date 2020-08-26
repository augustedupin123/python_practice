'''for i in reversed(range(1,6)):
    for j in reversed(range(i)):
        print(' ',end="")
    print('*'*5)
    print()'''


def shape1(num):
    for i in reversed(range(1,num)):
        for j in range(i):
            print(' ',end= ' ')
        print('*'*5)
        print()
shape1(5)