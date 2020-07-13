def sub_list(list1,list2):
    if(len(list1)>len(list2)):
        for i in range(len(list1)):
        if(list1[i]==list2[0]):
            if(list1[i:i+len(list2)]==list2):
                return True
    else:
        for j in range(len(list2)):
            if(list2[j]==list1[0]):
                if(list2[j:j+len(list1)]==list1):
                    return True

print (sub_list(['a','b','c','a','x','y','k','m','n','t','s','e'],['k','m','n','t','s','e']))

    
