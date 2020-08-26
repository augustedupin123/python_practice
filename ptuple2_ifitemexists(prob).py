#Write  program to check if an item exists in a tuple

'''def itemexistsornot(tuple1,t):
    count = 0
    for i in tuple1:
        if(i==t):
            return ('yes')
            count+=1
    if(count==0):
        return ('no')
print(itemexistsornot((232,23432,232,2335,235,23,235,235),(232)))'''

def item(tuple1,t):
    count = 0
    for i in tuple1:
        if(i==t):
            return('yes')
            count+=1
    if(count==0):
        return('no')
tuple2 = input('enter the tuple:')
m = input('enter the value to be checked')
item(tuple2,m)
        
        

 