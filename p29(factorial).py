def factorial(num1):
    flag = 1
    for i in range(1, num1+1):
        flag = flag*(i)
    return flag
a = int(input('Enter the number'))
x = factorial(a)
print(x)