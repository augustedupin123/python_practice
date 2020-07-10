#Write a program to get the largest number from a list

def largest(list1):
    maximum = 0
    for i in list1:
        if i > maximum:
            maximum = i
    return maximum
a = [53847597, -9235893475, 4589543238746365, 921890234]
print(largest(a))
