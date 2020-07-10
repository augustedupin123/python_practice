#Add 'ing' at he end of each string (length should be 3), if the string
#already ends with ing then add 'ly', drhkfgmjjlrlj,,jy,j,j,j,ghj,'gh,j'gh,g,jgghj'hgh

'''def string_add(str1):
    length = len(str1)
    if (length > 3):
        str = str1[-3:]
        if(str == 'ing'):
            str1 += 'ly'
        return str1
    
a = input('enter the string')
a = string_add(a)
print(a)'''

def string_add(str1):
    
    if (len(str1) > 3):
        
        if(str1[-3:] == 'ing'):
            str1 += 'ly'
        else:
            str1 += 'ing'
        return str1
    
a = input('enter the string')
a = string_add(a)
print(a)
