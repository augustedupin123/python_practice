#checking validity of password

def ifpasswordlegal(str1):
    flag = 0
    for i in range(65,91):
        if chr(i) in str1:
            flag = 1
    if(flag==0):
        return False
    count = 0
    for j in range(90,123):
        if chr(j) in str1:
            count = 1
    if(count==0):
        return False
    speciallist = ['@','#','$','^','*','!','(',')','&']
    val = 0
    for l in str1:
        if l in speciallist:
            val = 1
    if(val==0):
        return False
    if(flag==1 and val==1 and flag==1):
        return('Yes! The password is legal.')
print(ifpasswordlegal('sfg@jb'))
    
    