#Print the prime factors of a given no.

'''def prime_factors(num):
    for i in range(1,num):
        if(num%i == 0):
            for j in range(2, i):
                if(i%j !=0):
                    print (i)
                
a = int(input('num'))
prime_factors(a)'''

'''def primefac(num):
    mylist = []
    for i in range(1, num - 1):
        if(num%i==0):
            mylist.append(i)
    print (mylist)
a = int(input('enter num'))
primefac(a)'''

'''list = [2, 6, 9, 87, 51]
print(list[3])'''

'''list = [2, 3, 30, 5, 6, 7]
for i in list:
    print (i)
for i in range(len(list)):
    print (i)'''

def primefac(num):
    mylist = []
    facs = []
    for i in range(1, num - 1):
        if(num%i==0):
            mylist.append(i)
    for j in mylist:
        flag = 0
        for k in range(2, j):
            if(j%k==0):
                flag=1
                break
        if(flag == 0):
            facs.append(j)
    print(facs)



a = int(input('enter num'))
primefac(a)
