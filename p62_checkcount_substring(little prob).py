'''def nght(str1, str2):
    flag = len(str2)
    count = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if(str2[j] == str1[i]):
                if(str2[i:i+flag] == str2):
                    count+=1
        print (count)
a = input('enter str1')
b = input('enter str2')
nght(a,b)'''

'''def func(str1, str2):
    
    n2 = len(str2)
    count = 0
    for i in range(len(str1)):
        if(str1[i:i+n2] == str2):
            count+=1
    print(count)
a = input('enter a')
b = input('enter b')
func(a,b)'''

def func(m,n):
    x = 1
    count = 0
    for i in range(len(m)):
        for j in range(len(n)):
            if(n[j]!=m[i]):
                x = 0
            elif(x == 1):
                k = 0
                p = 0
                for k in range(0, len(n)+1):
                    if(m[i + k] == n[j + k]):
                        p = 1
                         
                
    if(p==1):
        print('yes')
    elif(p==0):
        print ('no')
a = input('enter string1')
b = input('enter string2')
func(a,b)


