def kth_largest_no(array, k):  
    array.sort()  # n^2
    return array[len(array) - k]
  
 
array = [90, 29, 10, 3, 20, 98, 100]  
k = 3
print(klargestno(array, k))

# try without sorting

'''
10000000
1 ms per input

1000000
'''