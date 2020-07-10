#Write a program to compute sum of digits of a given no.

def sum_of_digits(num1):
    rem1 = num1%10
    while(num1>0):
        num1 = int(num1/10)
        rem1 += num1%10
    print (rem1)
sum_of_digits(102)














'''x = 9762137
sum1 = x/10
val = int(sum1)
rem1 = x%10
print (val, rem1, sum1)'''

