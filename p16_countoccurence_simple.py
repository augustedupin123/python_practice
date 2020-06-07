def countoccurence(x,h):
    count = 0
    for i in range(len(x)):
        if(x[i] == h):
            count+=1
    print (count)
a = input('enter the string')
b = input('enter the character')
countoccurence(a,b)