#Longest subarray

def function_ab(st2):
    for i in range(len(st2)):
        for j in range(i+1,len(st2)):
            if(st2[j]==st2[i]):
                list2.append(j-i)
    print(list2)
function_ab('abdefgabef') 