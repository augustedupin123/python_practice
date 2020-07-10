#write a program to move all spaces to the front.

def move_spaces(str1):
    count = 0
    str2 = ''
    for i in range(len(str1)):
        if(str1[i]== ' '):
            count+=1
    for j in range(len(str1)):
        if(str1[j]!=' '):
            str2+=str1[j]
    print(' '*count + str2)
move_spaces('After completing my MS in USA I joined WalmartLabs')
            

