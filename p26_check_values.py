def var(x,y,z):
    if (x == y == z):
        return("same")
    else:
        return("not same")
a = input('enter x')
b = input('enter y')
c = input('enter z')
s = var(a,b,c)
print(s)
