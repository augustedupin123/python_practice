#Write a python program to reverse a string

'''def reverse_string(str1):
    for i in reversed(range(len(str1))):
        print (str1[i], end="")
a = input('enter the string')
reverse_string(a)

input - i love to eat caviar and steak
output - kaets dna raivac tae ot evol i 

'''

'''def string1(str2):
    x =  (str2[::-1])
    return x
a = input('enter string')
print (string1(a))'''

'''def function1(list1):
    for i in reversed(range(len(list1))):
        print (list1[i])
a = input('enter list').split()
function1(a)'''

def function1(str1):
    list2 = []
    for i in range(len(str1)):
        if(str1[i]!= ''):
            list2.append(i)
        else:
            while(len(list2) > 0):
                print(list2[:-1], end="")
            print(end = " ")
a = input('enter string')
function1(a)            











'''def string1(str):
    print(str)
a = input('str1')
string1(a)'''

    





