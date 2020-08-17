# Python program for implementation of Selection Sort 
# Pick each item and Compare with every other item and then swap if found greater than other items  
import sys 
A = [64, 25, 12, 22, 11] 

# Traverse through all array elements 
for i in range(len(A)): 
	
	# Find the minimum element in remaining unsorted array 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j
    
    A[i] = A[min_idx]
    A[min_idx] = A[i]
	# Swap the found minimum element with the first element		 
	# A[i], A[min_idx] = A[min_idx], A[i] 

# Driver code to test above 
print ("Sorted array: {}".format(A))
