'''
11111
2222
333
44
5
'''

'''for i in reversed(range(1,6)):
    m=5
    for j in (range(0, i+1)):
        print(m, end="")
        m -=1
    print()'''

for i in (range(1,6)):
    for j in range(0, 6 - i):
        print(i, end="")
    print()




