#Reverse the string if length of string is a multiple of 4

#def string_function(a):
#    print(len(a))
#m = input('enter the value of m')
#string_function(m)

def function1(m):
    if(len(m)%4 == 0):
        for i in reversed(m):
            print(i)
    else:
        print('string is not a multiple of 4')
a = input('enter the string')
function1(a)
    