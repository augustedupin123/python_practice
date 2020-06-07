#def fun1(x):
#    i = len(x) - 1
#    while(i>=0):
#        print(x[i])
#        i = i - 1
#y = input('ente the value of the string')
#fun1(y)
#Printing string in reverse order

"""def fun2(x):
    for i in (x):
        print(x[0], x[1], x[3])
y = input('enter a string')
fun2(y) 
why this output got displayed 3 times.."""

"""def fun2(x):
    for i in range(len(x)):
        print(x[0], x[1], x[3])
y = input('enter a string')
fun2(y)"""

def compare(x1, x2):
    flag = 1
    for i in range(len(x1)):
        for j in range(len(x2)):
            if(i==j):
                if(x1[i]==x2[j]):
                    flag = 0
    if(flag == 0):
        print("strings are equal")
    else:
        print("strings are unequal")
A = input('enter string1')
B = input('enter string2')
compare(A,B)






