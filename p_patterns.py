'''for i in range(5):
    print(i,end=" ")


for i in range(5):
    print(i,end="")

for i in range(5):
    print(i,end=" ")'''


'''for i in range(5):
    print(i,end=" ")
    print()'''

'''for i in range(1,1):
    print('*')'''


'''for i in range(3,9):
    for j in range(2,i):
        print('*',end="")
    print()'''


'''for i in range(1,7):
    for j in range(0,(2*i - 1)):
        print('*',end="")
    print()'''



'''def pattern1(num):
    for i in range(1,num+1):
        for j in range(0,(2*i - 1)):
            print('*',end="")
        print()
pattern1(5)

def pattern1_1(num):
    k = 1
    for i in range(1,num+1):
        for j in range(1,k+1):
            print('*',end="")
        k = k+2
        print()'''

'''def pyramid(num):
    for i in range(0,num):
        for j in range(0,num - i - 1):
            print(end=' ')
        for k in range(0,i+1):
            print('e',end=' ')
        print()
pyramid(5)'''

'''def ev_pyamid(num):
    for i in range(num,0,-1):
        for j in range(0,num-i):
            print(end=" ")
        for k in range(0,i):
            print('e',end=" ")
        print()
ev_pyamid(5)'''



'''#Full pyamid

def pyamidfull(num):
    for i in range(0,num):
        for j in range(0,num - i - 1):
            print(end=' ')
        for k in range(0,i+1):
            print('e',end=' ')
        print()



    for l in range(num,0,-1):
        for m in range(0,num-l):
            print(end=" ")
        for v in range(0,l):
            print('e',end=" ")
        print()
pyamid(5)'''

'''def pgm5_reverserighttriangle(num):
    for i in range(num,0,-1):
        for j in range(0,i):
            print('*',end='')
        print()
pgm5(5)'''

'''def onefourthofhollowpyramid(num):
    for i in range(num,0,-1):
        for j in range(0,i+1):
            if(j==i):
                print('*',end=' ')
                
                
            else:
                print(end=' ')
        print()
onefourthofhollowpyramid(5)'''
    
def func(num,num2):
    for i in range(num,0,-1):
        for j in range(0,i+1):
            if(j==i):
                print('*',end=' ')
            else:
                print(end=' ')    
        print()
    for m in range(0,num2+1):
        for n in range(0,m+1):
            if(n==m):
                print('*',end=' ')
            else:
#                print(end = ' ')
                print(end =' ')
        print()
func(5,5)
    













    
    

