#Write a python script to generate and print a number 
# in the form of (x,x*x)

def spldict(num1):
    dict1 = {}
    for i in range(1,num1+1):
        dict1.update({i:i*i})
    return (dict1)
print(spldict(5))
        
