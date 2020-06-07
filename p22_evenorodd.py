def even_or_odd(num):
    flag = num % 2
    if(flag > 0):
        return ('odd')
    else:
        return ('even')
a = int(input('enter the no.'))
x = even_or_odd(a)
print (x)
