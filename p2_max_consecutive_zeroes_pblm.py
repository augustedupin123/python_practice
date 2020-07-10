#Write a program to find max length of consecutive zeroes in a given
#binary string

'''def max_length_of_zeroes(str1):
    m = 0
    for i in range(len(str1)):
        if(str1[i]=='0'):
            for j in range(len(str1)):
                if(j>i and str1[j]=='1'):
                    m = max(j - i,m)
                    break

    print (m)
a = input('give values:')
max_length_of_zeroes(a)'''
                    

banti = '01100011100001'

list1 = []
count = 0
for i in range(len(banti)):
    
    if(banti[i] == '0'):
        for j in range(len(banti)):
            if(j>i and banti[j]=='1'):
                count = (j - i)
                list1.append(count)
                break
print (list1)

            
                

