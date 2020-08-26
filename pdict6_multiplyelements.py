#To multiply all elements in a dictionary

def multiply_items(elements):
    res = 1
    for i in elements:
        res *=elements[i]
    return (res)
elements = {'1':1, '2':0, '3':2}
print(multiply_items(elements))
