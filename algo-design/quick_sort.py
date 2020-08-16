# This function takes last element as pivot, places the pivot element at its correct position in sorted mylistay, 
# and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot 
def partition(mylist,low,high): 
	i = (low-1)
	pivot = mylist[high]
	for j in range(low , high): 
		if mylist[j] < pivot: 
			i = i+1
			mylist[i],mylist[j] = mylist[j],mylist[i] 

	mylist[i+1],mylist[high] = mylist[high],mylist[i+1] 
	return ( i+1 )

# Function to do Quick sort 
def quickSort(mylist,low,high):
	if low < high: 
		pivot = partition(mylist,low,high) 
		# Separately sort elements before partition and after partition 
		quickSort(mylist, low, pivot-1) 
		quickSort(mylist, pivot+1, high) 

mylist = [10, 7, 8, 9, 1, 5] 
n = len(mylist) 
quickSort(mylist,0,n-1) 
print (mylist) 