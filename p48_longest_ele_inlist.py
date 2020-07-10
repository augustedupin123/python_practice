#Write a python program that takes a list of given words and returns 
#the length of the longest one.

def longest_word(l):
    maximum = 0
    for i in l:
        if(len(i) > maximum):
            maximum = len(i)
    return (maximum)
a = ['hgdyhjbjkbjkbj', 'jhvhn', 'hfhnjkbjk', 'fhjkbjjkjhkkkk', 'jfuhvbjkbjjjjgbbbkyiyutyp']
m = longest_word(a)
print (m)

'''def function(l):
    print(l)
a = list(input('enter list elements').split())
list1 = []
list1.append(a)
function(list1)'''

