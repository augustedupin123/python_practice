#Concatenating 3 dictionaries

def concatenation(a,b,c):
    dict4 = {}
    for i in (a,b,c):
        dict4.update(i)
    return (dict4)

    
x = {'sgsrg':'fefzsdfs'}
y = {'sdgdrh':'saeg'}
z = {'sdgrd':'dfgrhh'}
print(concatenation(x,y,z))
    
    