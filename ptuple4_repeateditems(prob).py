#Write program to find repeated items of a tuple

'''def tuplerepeat(tuple1):
    list2 = []
    for i in range(len(tuple1)):
        if i in tuple1[i+1:]:
            list2.append(i)
    print(list2)
tuplerepeat((2,3,4,5,6,7,2,2,3,4,5,233,235,35,535))'''

'''def tuplerepeat(tuple1):
    list2 = []
    tuple3 = ()
    for i in range(len(tuple1)):
        if i in tuple1[i+1:]:
            list2.append(i)
    tuple3 = tuple(list2)
    print(tuple3)
tuplerepeat((2,3,4,5,6,7,2,2,3,4,5,233,235,35,535))'''

'''def tuplerepeat(tuple1):
    
    list2 = []
    tuple3 = ()
    for i in range(len(tuple1)):
        if tuple1[i] in tuple1[i+1:]:
            list2.append(tuple1[i])
    tuple3 = tuple(list2)
    return(tuple3)
tuple2 = input('enter tuple elements')
print(tuplerepeat(tuple2))
output problem'''



def tuplerepeat(list5):
    list2 = []
    
    
    tuple3 = tuple(list5)
    for i in range(len(tuple3)):
        if tuple3[i] in tuple3[i+1:]:
            list2.append(tuple3[i])
    tuple4 = tuple(list2)
    return(tuple4)
list5 = []

a = int(input('enter no. of tuple elements'))
for _ in range(a):
    l = input()
    list5.append(l)
print(tuplerepeat(list5))






    