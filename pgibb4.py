#write a program to find the maximum and minimum in a set

def gibb(list1):
    set1 = set(list1)
    max1 = 0
    min1 = 0
    for i in set1:
        if(i>max1):
            max1 = i
    for j in set1:
        if(j<min1):
            min1 = j
    print(max1,min1)
gibb([2,3,4,5,2,4,5,2,4,5,6,6,4,3846,234,2348])