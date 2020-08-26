#tennis = {'nadal':'spain','djokovic':'serbia','thiem':'austria', 'federer':'switzerland','fucdovics':'hungary','monfils':'france', 'kyrgios':'australia'}

#tennis.pop('fucdovics')

#print(tennis.keys())
#print(tennis.values())

#print (tennis.items())

#tennis1 = {'tommy haas':'germany', 'juan martin del potro':'argentina'}
#tennis.update(tennis1)
#print(tennis)

'''def dict_func(a):
    for i in a:
        print(i)
        print(a[i])
d = {'a':'1', 'b':'2', 'c':'3','d':'4'}
dict_func(d)'''

def getinput(num1):
    list1 = []
    s = set()
    for i in range(num1):
        p = input()
        list1.append(p)
    print(list1)
    for l in range(num1):
        q = input()
        s.add(q)
    print(s)

getinput(int(input('enter noofelements')))

