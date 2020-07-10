#Write a program to count the no. of strings where the string length is two
# or more and the first and last characters are the same from a given
#list of strings

def program(list1):
    count = 0
    for i in list1:
        if(len(i)>2 and i[0]==i[-1]):
            count+=1
    print (count)
program(['abc', 'skjdgdfg', 'sdkfhgs', 'aba'])
