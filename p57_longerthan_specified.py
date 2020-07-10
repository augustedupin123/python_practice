#Write a python program to find the list of words that are longer 
#than n from a given list of words.

def list_of_words(l,n):
    listreq = []
    l1 = l.split()
    for i in l1:
        if len(i)>n:
            listreq.append(i)
    return listreq
a = input('enter the list')
n1 = int(input('enter n'))
print (list_of_words(a,n1))

