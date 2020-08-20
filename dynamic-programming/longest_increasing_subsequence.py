# Dynamic programming Python implementation of LIS problem 

# lis returns length of the longest increasing subsequence in arr of size n 
def lis(arr): 
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
print ("Length of arr is ", lis(arr))
print ("Length of arr1 is ", lis(arr1))
print ("Length of arr2 is ", lis(arr2))
