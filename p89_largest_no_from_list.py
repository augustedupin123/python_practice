#Write a program to find the largest number from a list

def largest_list(list1):
    lar = 0
    for i in list1:
        if(i>lar):
            lar = i
    print (lar)
a = largest_list([94, -40, -990, 59, -50, -900])