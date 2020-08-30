#Given an integer array and an integer S, find the no. of sub arrays where all the elements
# are less than S

def facebook_question(list1,s):
    t = 0
    for i in range(len(list1)):
        for j in range(len(list1),i,-1):
            w = 1
            for k in list1[i:j+1]:
                if(k>s):
                    w = 0
            if(w==1):
                t+=1
                print(list1[i:j])
    return(t)
if __name__=='__main__':
    list1 = [1,2,3,4,5,6,7]
    l = 5
    print(facebook_question(list1,l))

                

  
