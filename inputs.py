# def list_input(n):
#     # return a list of length n with user inputs for each index
#     l = []
#     print('availabale datatypes : int, string, float')
#     print("Enter i for integer, s for string, f for float")
#     for _ in range(n):
#         d = input('what datatype you want : ')
#         if d == 'i':
#             l.append(int(input(f"Enter integer: ")))
#         if d == 'f':
#             l.append(float(input(f"Enter decimal: ")))
#         if d == "s":
#             l.append(input(f"Enter decimal: "))
#     return l

def list_input(n):
    # return a list of length n with user inputs for each index
    l = []
    for _ in range(n):
        l.append(int(input()))
    return l

def str_input():
    return input("Enter string : ")
# print(list_input(5))