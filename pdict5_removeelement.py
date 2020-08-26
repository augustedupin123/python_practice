#From a dictionary remove an element

def removelement(dict2,m):
    del dict2[m]
    return (dict2)
dict2 = {'satnamsingh':'basketball', 'pogba':'france', 'bhupati':'tennis', 'paes':'tennis'}
m = 'paes'
print(removelement(dict2,m))