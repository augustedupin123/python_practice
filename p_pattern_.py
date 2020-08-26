num = 5

for i in range(num,0,-1):
    for j in range(0,num-i):
        print('*',end=" ")
    print('a'*(2*i-3)*2,end=" ")
    for k in range(0,num-i):
        print('*',end=' ')
    print()

    

    