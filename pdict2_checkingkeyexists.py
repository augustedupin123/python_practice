#Check whether a key exists in a dictionary or not

def checkexists(dict1,m):
    if m in dict1:
        return ('yes')
    else:
        return ('no')
dict2 = {'a':1,'b':2,'c':10}
b = 'c'
print(checkexists(dict2,b))
            

