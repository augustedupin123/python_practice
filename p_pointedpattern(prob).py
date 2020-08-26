'''num = 5
for i in range(num):
    for j in range(num-i):
        print(' ',end=" ")
    print('*',end=" ")
    print(' '*(2*i - 1)*2,end=" ")
    print('*')
    print()'''


num = 5

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end=" ")
    print('*',end=" ")
    print(' '*(2*i - 3)*2,end=" ")
    
    print('*')
    print()


for l in range(num):
    for m in range(num-l):
        print(' ',end=" ")
    print('*',end=" ")
    print(' '*(2*l - 1)*2,end=" ")
    print('*')
    print()
