#Write a program to count the no. of strings where the length of string is 
# 2 or more and where the first and last characters are the same.

def countstrings(list1):
    count = 0
    list2 = list1.split()
    print (list2)
    for i in list2:
        if (len(i)>=2 and i[0] == i[-1]):
            count+=1
        
    return count
a = input('Enter the list elements')
y = countstrings(a)
print(y)