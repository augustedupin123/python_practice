# def num(n):
#     if n > 0 :
#         return 'positive'
#     elif n < 0 :
#         return 'negative'
#     else:
#         return '0'

# x = float(input('Enter the required number : '))

# print(num(x))



# check palindrome

def check_palindrome(s):
    """
    take the original string
    iterate it reversively
    store the characters incresingly in reverse order
    check if the new string and the old one are same
    """

    # Complexity : n
    # if s == s[::-1]:
    #     return True
    # return False

    # complexity = n/2
    if s[0 : len(s)//2] == s[len(s) : len(s)//2 : -1]:
        return True
    return False

    # complexity = n/2
    # works both for even and odd
    # for i in range(len(s)//2):
    #     if s[i] == s[-i-1]:
    #         pass
    #     else:
    #         return False
    # return True

print(check_palindrome(input("enter string to check palindrome : ")))


"""

list
    iterable - collection of more than one references
    []
    different types of data can be there at every index
    mutable
    indexed

string
    iterable - collection of more than one references
    '', "" -> single line
    """ """, ''' ''' -> multilined strings
    at every index there should be only one character
    immutable
    indexed


character are 256 in number, defined by ASCII

"""