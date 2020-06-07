def sum_of_cubes(num):
    sum1 = 0
    for i in range(0, num):
        sum1 += (i*i*i)
    return sum1
a = int(input('enter value of the no.'))
h = sum_of_cubes(a)
print(h)
