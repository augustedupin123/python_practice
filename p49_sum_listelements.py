#Write a program to add all elements in a list

def sumelements(list1):
    sum1 = 0
    for i in list1:
        sum1 = sum1 + i
    return sum1
a = [1, 3, -10, -40]
print(sumelements(a))