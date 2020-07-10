#Write a program that takes 2 lists and returns true if they have a common member

def listcommon(l1,l2):
    x = 0
    for i in l1:
        for j in l2:
            if(i==j):
                x = 1
                return x
print (listcommon([1, 559, 23235, 4564557], [3, 1, 456456]))
