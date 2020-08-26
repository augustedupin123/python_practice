def printoutput(str1):
    for i in range(len(str1)):
        if(ord(str1[i])==117):
            print(chr(92),end="")
        if(ord(str1[i])==68):
            print(chr(47),end="")
        else:
            print('m',end="")
        
            
printoutput('udghtudhtytueit')


'''var = 'a'
print(ord(var))'''
