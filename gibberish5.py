"""def fun2(x):
    for i in range(len(x)):
        print(i + 1)
y = input('enter a string')
fun2(y)"""

"""def function1(x):
    for i in (x):
        if(i < 2):
            return i
        else:
            return 0
        
y = input('enter a string')
function1(y)"""

'''def fun(x):
    for i in range(len(x)):
        print(x[i+1])
y = input('enter the string')
fun(y)

#Problem here
lnsdlcnsldnclsnclksnclskcnlkslcnsc'''

list1 = [1,2,4,5,6,88,100]
for i in range(len(list1)):
    for j in range(len(list1)):
        if(j!=i):
            print(list1[j])
