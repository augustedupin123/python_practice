#Write a program to reverse a tuple

def reversetuple(tuple1):
    list2 = []
    for i in reversed(range(len(tuple1))):
        list2.append(tuple1[i])
    tuple2 = tuple(list2)
    return(tuple2)
n = int(input('enter no. of tuple elements'))
list1 = []
for _ in range(n):
    l = input()
    list1.append(l)
tuple3 = tuple(list1)
print(reversetuple(tuple3))

