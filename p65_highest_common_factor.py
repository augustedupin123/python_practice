#LCM and HCF
#hcf

def func(num1,num2):
    list1 = []
    list2 = []
    max1 = 0
    for i in range(1, num1):
        if(num1%i==0):
            list1.append(i)
    for j in range(1, num2):
        if(num2%j==0):
            list2.append(j)
    print (list1)
    print (list2)
    list3 = []
    for k in list1:
        for l in list2:
            if(k==l):
                list3.append(k)
    print (list3)
    for m in list3:
        if(m>max1):
            max1 = m
    print(m)

        


a = int(input('enter num1'))
b = int(input('enter num2'))
func(a,b)
        