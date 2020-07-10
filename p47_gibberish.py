#Print all unique words in a string
mylist = []
str1 = ""
string2 = input('enter the string')
for i in range(len(string2)):
    if(string2[i] == " "):
        mylist.append(str1)
        str1 = ""
    else:
        str1 += str(string2[i])
    if(str1!= None):
        mylist.append(str1)
print(mylist)
