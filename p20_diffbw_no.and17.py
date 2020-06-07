def diff(num):
    if(num<=17):
        return (17 - num)
    else:
        return(num - 17)
a = int(input('please enter the value of number'))
x = diff(a)
print(x)
