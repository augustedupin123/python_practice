#Get a string from a given string where all occurances of the first char has been changed to
#'@' except the first char itself 

def string_change_occurances(m):
    char = m[0]
    m = m.replace(char, '@')
    m = char + m[1:]
    print(m)
x = input('string:')
string_change_occurances(x)
