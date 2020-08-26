def swapevenodd(list1):
    for i in range(len(list1)):
        if(i%2!=0 and list1[i]<list1[i-1]):
            list1[i], list1[i-1] = list1[i-1],list1[i]
    print(list1)
swapevenodd([5,4,3,2,1])