#  Write a Python program to test whether all numbers of a list is greater than a certain number.

 def greater_than_certain(list_of_numbers, comp_num):
     list_of_numbers_greater_than_num = []
     for number in list_of_numbers:
         if number > comp_num:
             list_of_numbers_greater_than_num.append(number)
     return list_of_numbers_greater_than_num
      for i in list_of_number:
          if(i < num):
              break
#      return True

 list_of_numbers = list(map(int, input('Enter numbers separated by space :').split()))
 comp_num = int(input("Enter to be compared number : "))
 print(greater_than_certain(list_of_numbers, comp_num))

'''
input - list of numbers, number'''


'''# list = ['prasant', 'bangalore', '@435435']
def list_input(n):
    return_list = []
    for i in range(n):
        return_list.append(input(f"Enter element at position {i} : "))
    return return_list
print(list_input(5))

#terminal -> powershell, cmd, bash, zsh, csh'''