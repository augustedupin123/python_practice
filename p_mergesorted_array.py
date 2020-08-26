'''check which list is longer, and then put the elements fro the smaller list to the biger list
extend same number of 0's as the length of the shorter list'''

[1,2,3,4],[2,5,6]

'''def merge_zeros(l1, l2):
    l1.extend([0]*len(l2))
    return l1, l2'''


def listoper(list1,list2):
    for k in range(len(list2)):
        
        for l in range(len(list1)- 1):
            if(list2[k]>list1[l] and list2[k]<list1[l+1] or list2[k]==list1[l]):
                list1.insert(l+1,list2[k])
                print('hi')
                
            else:
                if(list2[k]>list1[-1]):
                    list1.append(list2[k])
                    print('abc')


    return (list1)
print(listoper([1,20,29,37],[2,20,21,23,48,50]))

i = 0
j = 0
list1[i]<list1[j]
while(i<n1 and j<n2):
    if(list1[i]<list2[j]):
        list2.insert(j,list1[i])
    else:
        
    

            

            


'''def merge_sorted_array(l1, l2):
    if len(l1) > len(l2):
        l1, l2 = merge_zeros(l1, l2)
    else:
        l1, l2 = merge_zeros(l2, l1)
    print(listoper(l1,l2))
    # write code here
if __name__ == "__main__":
    print(listoper([11,12,13,24,28,32], [14,25,31]))''' 


    