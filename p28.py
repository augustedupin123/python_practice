def greater_than_certain(set,num):
    for i in set:
        if(set[i] < num):
            print('all nos. are not greater')
            break;
        else:
            print('yes all nos. are greater than in the list')
a = list(input('enter the list of nos.'))
b = list(input('enter the value of num'))
greater_than_certain(a,b)
