#Write a program to check whether a sublist is present in the list or not

def check_sublist(list1,list2):
    b = len(list1)
    c = len(list2)
    
    


    for i in range(len(list1)):
        
        if(list1[i] == list2[0]):
            for j in range(c):
                if(i+j==b):
                    break
                else:

                    if(list1[i+j]==list2[j]):
                        print ('probably')
                        break
                    
                    
    
check_sublist([0,2,3,4,5,6,7,8,9],[2,3,4,5,6])
        
    