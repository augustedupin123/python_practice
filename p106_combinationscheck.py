'''def checkcombinations(list1):
    n = len(list1)
    for i in range(1,len(list1)):
        for j in range(i+1,n+1):
            print ([i,j])
checkcombinations([1,2,3,4,5,6,7])'''

def printcombinations(list1):
    n = len(list1)
    for i in range(n):
        for j in range(i+1,n+1):
            for k in range(j+1,n+2):
                print ([i,j,k])
printcombinations([1,2,4,5,6,7,8,9,10])


