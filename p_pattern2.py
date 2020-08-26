num = 5
for i in range(num,0,-1):
    for j in range(num-i):
        print(' ',end="")
    print('*'*(2*i-1),end=" ")
    print()

for l in range(num+1):
    for s in range(num-l):
        print(' ',end="")
    print('*'*(2*l-1),end=" ")
    print()



'''num = 5
for l in range(num,0,-1):
    for j in reversed(range(num-l)):
        print(' ',end="")
    print('*'*(2*l-1),end="")
    print()'''
'''num = 4
for i in reversed(range(num)):
    for j in range(i):
        print(' ',end=" ")
    print('*'*(2*i+1),end=" ")
#    for l in range(i):
#        print(' ',end=" ")
    print()'''


'''num = 4
for i in reversed(range(num)):
    for j in range(num):
        for k in range(i):
            print(' ',end=" ")
        print('*'*(2*j+1)*2,end=" ")
        for l in range(i):
            print(' ',end=" ")
        print()'''
'''num = 4
i = 4
j = 0
while(i>-1 and j <num):
    for j in range(i):
        print(' ',end="")
    print('*'*(2*i+1),end="")
    print()
    i-=1
    j+=1'''



