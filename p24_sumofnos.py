def sum_of_nos(x,y,z):
    sumreq = x + y + z
    if(x==y or y==z or x==z):
        sumreq = 0
    return sumreq
a = float(input('enter x'))
b = float(input('enter y'))
c = float(input('enter z'))
m = sum_of_nos(a,b,c)
print(m)