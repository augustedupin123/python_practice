#Window

def window(str1,str2):
    str4 = ''
    str5 = ''
    for i in range(len(str1)):
        if (str1[i] not in str1[i+1:]):
            str4+=(str1[i])
    for i in str2:
        for j in str1:
            if(j==i):
                str5+=str(j)
                

                


    
    print (str4)
window('kdbdbfnokfghkorthj')
