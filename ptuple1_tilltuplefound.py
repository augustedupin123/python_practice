#Write a program to count the elements in a list until the element is a tuple

def countelements(list1):
    count = 0
    for i in list1:
        if i is not tuple:
            count+=1
        else:
            break
    return(count)
list1 = ([2,2,3,(2,3,4,5)])
print(countelements(list1))

        
            

