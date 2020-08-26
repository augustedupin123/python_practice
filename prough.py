#n = int(input('enter the value of n'))
N = int(input('enter the value of n:'))
str1 = input('enter the string')
n = len(str1)
list1 = list(str1)
for i in range(1,n-1):
    if(list1[i]!=' '):
        if(list1[i]==list1[i+1] or list1[i]==list1[i-1]):
            print('solution not possible')
            break

for j in range(len(list1)):
    if(list1[j]==' '):
        list1[j] = 'B'
string5 = ''.join([str(l) for l in list1])
print(string5)

    
