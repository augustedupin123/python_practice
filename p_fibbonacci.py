def fibbonaci(N):
    a = 0
    b = 1
    i = 0
#    print(a)
#    print(b)
    while(i<N):
        print(a)
        k = a + b
        a = b
        b = k
        i = i+1
fibbonaci(7)

