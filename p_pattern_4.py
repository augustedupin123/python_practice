num = 5
for i in range(6):
    for j in range(0,i):
        print('*',end=" ")
    for k in range(num,0,-1):
        print('0',end=" ")
    num -=1
    print()

