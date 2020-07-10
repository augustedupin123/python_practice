#Write a program to change every nth value to (n+1)th value in a list

def change_values(list1):
    
    for i in range(len(list1)):
        temp = 0
        if(list1[i]%2!=0):
            temp = list1[i]
            list1[i] = list1[i-1]
            list1[i-1] = temp
    print (list1)
change_values([0,1,2,3,4,5,6,7,8])


        