#Write a program sublists of a given list

'''def sub(list1):
    for i in reversed(range(len(list1))):
        for j in range(i+1):
            print (list1[j])
        print ()
        
sub([113,151,179,183,187])'''

'''def skldfsg(list1):
    for k in range(len(list1)):
        for i in reversed(range(len(list1) - k)):
            for j in range(i+1):
                print (list1[j])
            print ()
skldfsg([113,151,179,183,187])'''

def function(list1):
    n = len(list1)
    for i in range(len(list1)):
        for j in range(i,n):
            for k in range(i,j+1):
                print(list1[k])
            print ()
function([113,151,179,183,187])



        

