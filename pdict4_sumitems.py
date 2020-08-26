#Write a python program to sum all items in a dictionary

def sumitems(dict1):
    sum1 = 0
    for i in dict1:
        sum1+=dict1[i]
    print(sum1)
sumitems({'s':2,'g':2})

    