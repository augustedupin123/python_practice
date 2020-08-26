#Print key with max value in dictionary

def func(d):
    for i in d:
        print(i, d[i])
    realvalues = d.values()
    print(max(realvalues))
D = {'a':100, 'b': -50, 'c':120}
func(D)