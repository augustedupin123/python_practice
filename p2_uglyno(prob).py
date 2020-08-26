'''def nbiggar(num1):

    list1 = []
    list2 = []
    list4 = []
    for i in range(1,num1+1):
        if(num1%i==0):
            list1.append(i)
    list1.remove(1)
    for j in list1:
        flag=0
        for k in range(2,j):
            if(j%k==0):
                flag = 1
        if(flag==0):
            list2.append(j)
    for l in list2:
        val = 0
        if(l!=2 or l!=3 or l!=5):
            val = 1
        if(val==0):
            list4.append(val)
    if(len(list4)==0)):
        print('this is an ugly no.')
nbiggar(15)'''


def uglyab(num1):
    
        count = 0
        list1 = []
        list2 = []
        list4 = []
        for i in range(1,num1+1):
            if(num1%i==0):
                list1.append(i)
        list1.remove(1)
        for j in list1:
            flag=0
            for k in range(2,j):
                if(j%k==0):
                    flag = 1
            if(flag==0):
                list2.append(j)
        print(list2)
        for l in list2:
            val = 0
            if(l!=2 and l!=3 and l!=5):
                val = 1
            if(val==1):
                list4.append(val)
        if(len(list4)==0):
            count+=1
            print(i,'this is an ugly no.')
            print(count)
        else:
            print('no')
        
        
uglyab(6)

    
        