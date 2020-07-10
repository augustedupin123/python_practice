#Write a program to capitalize first and last letters of each word of a given string

'''def func(str1):
    list1 = str1.split()
    for i in list1'''

'''def func1(str1):
    list1 = str1.split(" ")
    print (list1[5])
    for j in list1[5]:
        print (j)
a = input('enter string elements')
func1(a)'''

'''def capitalize(str1):
    list1 = str1.split(" ")
    str2 = ''
    
    for word in list1:
        str2+= chr(ord(word[0]) + 32)
        
    print (str2)
    
        
        
        
            
a = input('enter values')
capitalize(a)'''

string1 = 'sanfrancisco toledo ontario skldf asdfsdfn sfsfdgkj'
string2 = ''

'''for word in string1.split():
    string2+= word[0].upper() + word[1:-1] + word[-1].upper() + ' ' 
print (string2)'''

string2 = ''

for word in string1.split():
    string2+= chr(ord(word[0]) - 32) + word[1:-1] + chr(ord(word[-1]) - 32) + ' '
print (string2)



    
    






