#If a number is power of another no. without using pow

def function1(a,b):
    prod = 1
    while(prod<b):
        prod *=a
    if(prod == b):
        print('the no. is a power')
    else:
        print('the no. is not a power')
        
            
    
m = int(input('enter a'))
n = int(input('enter b'))
print (function1(m,n))

