#tbd later

def pt(string2):
    w = '('
    count = 0
    f = 0
    for i in range(len(string2)):
        for j in range(0,i):
            if(string2[j]==w):
                count+=1
        for l in range(i,len(string2)):
            if(string2[l]==w):
                f+=1
        if(f==count):
            print(i)
pt('(((())(((')




