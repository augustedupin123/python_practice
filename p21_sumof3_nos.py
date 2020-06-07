def sumof3(x,y,z):
    sum = x + y + z
    if(x==y==z):
        sum = sum*3
    return sum
print (sumof3(10000000,10000000,100000))