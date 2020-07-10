#Count the occurance of a particular character and find the length of a string.

#def length_of_string(str1):
#   count = 0
#    for i in str1:
#        count+=1
#    return count
#print(length_of_string('mohammedbinsalmanbinabdulaziz'))

'''def roughstring(abc):
    for i in abc:
        print(abc)
a = input('enter abc')
roughstring(a)'''

'''def roughstring(abc):
    for i in abc:
        print(str(i))
a = input('enter abc')
roughstring(a)'''

'''def roughstring(abc):
    for i in abc:
        print (i)
a = input('enter the string')
roughstring(a)'''

def roughstring(abc):
    count = 0
    for i in abc:
        if (i== " "):
            count+=1
    print('no of times space occurs is:')
    print (count)
a = input('enter the string')
roughstring(a)








