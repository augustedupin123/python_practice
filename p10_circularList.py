# def ci_identical(list1, list2):  
#     '''
#     length of both the lists are equal
#     are the elements have the same frequency

#     '''
#   list1.extend(list1) 
	
#   for i in range(len(list1)): 
	
#     if list2 == list1[i: i + len(list2)]: 
   
#       return True
#   return False

def identify_circular(l1, l2):
	if len(l1) != len(l2):
		return False
	else:
		for i in range(len(l2)):
			if l2[i] not in l1:
				return False
			else:pass
				# zeroth = l1[0]
				# l1 = l1[1:len(l1)]
				# l1.append(zeroth)
				# print(l1, l2)
				# if l2 == l1:
				# 	return True
		
		# i=0
		# while(i <= len(l1)):
		# 	zeroth = l1[0]
		# 	l1 = l1[1:len(l1)]
		# 	l1.append(zeroth)
		# 	print(l1, l2)
		# 	if l2 == l1:
		# 		return True
		# 	else:
		# 		i+=1
		# return False
  
list1 = [6, 6, 0, 0, 6] 
list2 = [6, 6, 6, 0, 0] 
list3 = [5, 6, 6, 0, 0] 

if(identify_circular(list1, list2)): 
	print("Yes") 
else: 
	print("No") 
	
if(identify_circular(list2, list3)): 
	print ("Yes")  
else: 
	print ("No")  