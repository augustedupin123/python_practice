#Write a program to combine two dictionary adding values for common keys

def addvalues(d1,d2):
    d3 = {}
    for i in range(1,len(d1)+1):
        for j in range(1,len(d2)+1):
            if(d1[i]==d2[j]):
                d3.update(d1[i]+d2[j])
            else:
                d3.update(d1[i])
    return (d3)
print(addvalues({'a':100,'b':'200','c':5},{'a':100,'b':200,'f':'200'}))