#Print the smallest window that prints the characters of the string itself

def shortestwindow(str1):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(str1)):
        for j in range(len(str1),i,-1):
            list1.append(str1[i:j])
    for k in range(len(str1)):
        if str1[k] not in str1[k+1:]:
            list2.append(str1[k])
    for s in range(len(list1)):
        val = 0
        for x in list2:
            if x not in list1[s]:
                val = 1
        if(val==0):
            list3.append(list1[s])
    return(len(min(list3, key=len)))
if __name__ == "__main__":
    print(shortestwindow('aaaaaaaaabcbcdbca'))



         
