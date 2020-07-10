#Find LCM of a number

'''def lcm(num1, num2):
    list1 = []
    i = 1
    if(num2%num1==0):
        print (num2)
    for i in range(1, num1*num2+1):
        if(i%num1==0 and i%num2==0):
            print (i)
            break
a = int(input('enter num1'))
b = int(input('enter num2'))
lcm(a,b)'''

def lcm(num1, num2):
    i = min(num1,num2)
    while(1):
        if(i%num1 == 0 and i%num2==0):
            break
        i+=1
    print (i)
a = int(input('enter num1'))
b = int(input('enter num2'))
lcm(a,b)

    
        

