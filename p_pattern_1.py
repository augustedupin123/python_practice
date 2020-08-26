'''for i in range(0,2):
    print('0'*2,end="")
    print('+',end="")
    print('0'*2,end="")
    print()
    print('+'*2,end="")
    print('0',end="")
    print('+'*2,end="")
    print()
    print('0'*2,end="")
    print('+',end="")
    print('0'*2)'''

num=7
for i in range(1,num+1):
    if(i==(num//2+1)):
        print('+'*2,end="")
        print('0',end="")
        print('+'*2,end="")
        print()
    else:
        print('0'*2,end="")
        print('+',end="")
        print('0'*2,end="")
        print()
    
    