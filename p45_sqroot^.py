'''def sq_root(num1):
    i = 1
    result = 1
    while(i<=num1):
        i = result*result
        i+=1
        result+=1
    return(result - 1)
a = int(input('enter no.'))
q = sq_root(a)
print(q)'''





def sqroot(num):
    mylist = []
    facs = []
    for i in range(1, num - 1):
        if(num%i==0):
            mylist.append(i)
    for j in mylist:
        if(j*j==num):
            return j
a = int(input('enter the no.:'))
x = primefac(a)
print(x)
