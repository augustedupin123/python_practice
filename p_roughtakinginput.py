'''def input_list(num1):
    list1 = []
    
    for i in range(num1):
        list1.append(int(input()))
    return list1
a = int(input('enter the no. of elements'))
print(input_list(a))'''
    

def input_list(num1):
    list1 = []
    
    for i in range(num1):
        list1.append(input())
    return list1
a = int(input('enter the no. of elements'))
#print(input_list(a))
b = str(input_list(a))

#b = tuple(input_list(a))
print(b)

    