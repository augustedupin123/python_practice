"""def uniquechar(x):
    for i in range(len(x)):
        for j in (i+1,x):
            if(x[j] != x[i]):
                print(x[j])
a = input('enter string')
uniquechar(a)

#problem"""

"""def uniquechar(x):
    answerstring = ""
    for i in range(len(x)):
        if(x[i] in answerstring):
            answerstring += x[i]
    print(answerstring)
a = input('string:')
uniquechar(a)"""

def uniqulement(x):
    answerlist = []
    for i in range(len(x)):
        if(x[i] not in answerlist):
            answerlist.append(x[i])
    print("List after removing duplicates: {}".format(answerlist))
a = input('enter the string')
uniqulement(a)




