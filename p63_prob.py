#Write a Python program to find the first 
#appearance of the substring 'not' and 'poor' from 
# a given string, if 'not' follows the 'poor', replace 
# the whole 'not'...'poor' substring with 'good'. Return the 
# resulting string. 

'''def specialfunc(str1):
    if ('not' in str1 and 'poor' in str1):
        print('yes')
    else:
        print ('no')
a = input('enter string')
specialfunc(a)'''

'''def specialfunc(a):
    str1 = 'not'
    str2 = 'poor'
    for i in range(len(a)):
        if(a[i:i+3]==str1):
            print(i)
    
m = input('enter a')
specialfunc(m)'''

'''def specialfunc(a):
    k = 0
    l = 0
    str1 = 'not'
    str2 = 'poor'
    if('not' in a and 'poor' in a):
        for i in range(len(a)):
            if(a[i:i+3]==str1):
                k = i
    print (k)
        for j in range(len(a)):
            if(a[j:j+3]==str2):
                l = j
    if(l>k):
        return (a[0:str[k]] + 'good' + a[str[l+3]:])
            
a = input('enter the string')
print (specialfunc(a))'''

def specialfunc(a):
    k = 0
    l = 0
    str1 = 'not'
    str2 = 'poor'
    if('not' in a and 'poor' in a):
        for i in range(len(a)):
            if(a[i:i+3]==str1):
                k = i
        print (k)
        for j in range(len(a)):
            if(a[j:j+4]==str2):
                l = j
        print (l)
    if(l>k):
        return (a[0:str[k]] + 'good' + a[str[l+3]:])
print (specialfunc('the not in poor'))

   




