def del_element(l,num):
    print(l)
    l.pop(0)
    print(l)
    l.pop(3)
    print(l)
    return l
    

#l = [i for i in range(15)]
l = [0, 1, 2, 3, 4, 5]
# [1,2,4,5]
idx = [0, 3]
print(del_element(l, idx))

# [1,2,4,6,8,9,10,12,13,14]