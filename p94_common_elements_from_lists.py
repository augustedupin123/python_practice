#Write a program to find common elements from 2 lists

def common_elements(list1,list2):
    list3 = []
    for i in list1:
        if(i in list2):
            list3.append(i)
    print (list3)
common_elements([3,5,40,55,47,21],[3,4534,40,47])
        
            
                
