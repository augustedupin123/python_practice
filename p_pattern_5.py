'''num = 5

for i in range(1,6):
    for j in range(num-i):
        print('*',end="")
        print(' '*(i-2)*2,end="")
        print('*')
        print()'''

n = int(input('enter no. of rows'))
for row in range(n):
    for col in range(n):
        if(col==0 or row==(n-1) or row==col):
            print('*',end="")
        else:
            print(end=" ")
    print()