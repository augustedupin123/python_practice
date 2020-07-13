from math import ceil, floor
def reverse_list(list1):
  k = 0
  for i in range(len(list1)-1, -1 , -1):
    temp = 0  
    temp = list1[i]
    list1[i] = list1[k]
    list1[k] = temp
    k +=1
    print(list1)
  return list1
    
if __name__ == "__main__":
  size = int(input("Enter size : "))
  list1 = list(map(int, input().split()))[:size]
  print(reverse_list(list1))

#  1 2 3 4 5
# 5 2 3 4 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 2 3 4 1
# 1 2 3 4 5

# floor(len(list1)/2)