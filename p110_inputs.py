'''def list_input(n):
    # return a list of length n with user inputs for each index
    l = []
    for _ in range(n):
        l.append(int(input()))
    return l

def str_input():
    return input("Enter string : ")
# print(list_input(5))'''

def func_input(n):
    m = []
    for _ in range(n):
        m.append((input()))
    return m

print (func_input(5))



from inputs import list_input

def check_duplicate(l):
    # which element is duplicate
    # it what index the duplicate element is there
    for i in range(len(l)):
        if l[i] in l[i+1 : ]:
            return True
    return False

if check_duplicate(list_input(6)):
    print("Duplicate found")
else:
    print("Duplicate not found")

def str_input():
    return input("Enter string : ")
# print(list_input(5))