#Write a program to multiply all items of a list

def multiplyitems(list1):
    z = 1
    for i in list1:
        z = z*i
    return z
a = [1, 3, 5, 40]
print(multiplyitems(a))