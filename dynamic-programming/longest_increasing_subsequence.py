# Dynamic programming Python implementation of LIS problem 
# lis returns length of the longest increasing subsequence in arr of size n 

def maxLIS(arr): 
	n = len(arr) 

	# Declare the list (array) for LIS and 
	# initialize LIS values for all indexes 
	lis = [1]*n 

	# Compute optimized LIS values in bottom up manner 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and lis[i] < lis[j] + 1 : 
				lis[i] = lis[j]+1

	# Initialize maximum to 0 to get 
	# the maximum of all LIS 
	maximum = 0

	# Pick maximum of all LIS values 
	for i in range(n): 
		maximum = max(maximum , lis[i]) 

	return maximum 
# end of lis function 

# Driver program to test above function 
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
arr1 = [16, 3, 5, 19, 10, 14, 12, 0, 15]
arr2 = [10, 8, 6, 4, 2, 0]
print ("LIS length of arr is ", maxLIS(arr))
print ("LIS length of arr1 is ", maxLIS(arr1))
print ("LIS length of arr2 is ", maxLIS(arr2))

##############################################################################################

# Given a list of N integers find the longest increasing subsequence in this list.
# Example
# If the list is [16, 3, 5, 19, 10, 14, 12, 0, 15] 
# one possible answer is the subsequence [3, 5, 10, 12, 15], another is [3, 5, 10, 14, 15].
# If the list has only one integer, for example: [14], the correct answer is [14].
# One more example: [10, 8, 6, 4, 2, 0], a possible correct answer is [8].

# Function to print the longest increasing subsequence
def lisNumbers(arr): 
	
	n = len(arr) 
	# Declare the list (array) for LIS and 
	# initialize LIS values for all indexes by 1
	lis = [1]*n 
	

	# Compute optimized LIS values in bottom up manner 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and lis[i] < lis[j] + 1 : 
				lis[i] = lis[j]+1
	# print(arr)
	# print(lis)
	myLISlist = []

	# Print the LIS sequence from all LIS values 
	for i in range(0, len(lis)): 
		if(i == 0):
			myLISlist.append(arr[0])
		elif(i > 0 and lis[i] == lis[i-1]):
			if(arr[i] > arr[i-1]):
				myLISlist.append(arr[i-1])
			else:
				myLISlist.remove(arr[i-1])
				myLISlist.append(arr[i])
		elif(i > 0 and lis[i] > lis[i-1]):
			myLISlist.append(arr[i])


	print myLISlist 

lisNumbers([10, 22, 9, 33, 21, 50, 41, 60])
lisNumbers([16, 3, 5, 19, 10, 14, 12, 0, 15])
lisNumbers([10, 8, 6, 4, 2, 0])