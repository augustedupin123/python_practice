'''num = 8

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end=" ")
    print('*',end=" ")
    print(' '*(2*i - 3)*2,end=" ")
    
    print('*')
    print()'''

    
'''num = 8

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end=" ")
    print('*',end=" ")
    print(' '*(2*i - 3)*2,end=" ")
    if(i!=num-1):
        print('*')
        print()
#    print('*')
#    print()'''

'''num = 8

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end=" ")
    print(i,end=" ")
    print(' '*(2*i - 3)*2,end=" ")
    
    print(i)
    print()'''

'''num = 8

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end=" ")
    print(num-i+1,end=" ")
    print(' '*(2*i - 3)*2,end=" ")
    
    print(num-i+1)
    print()'''


num = 8

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end="")
#    print(' '*(num-i-1))
    print(num-i+1,end=" ")

    print(' '*(2*i - 3)*2,end=" ")
    
    print(num-i+1)
    print()
