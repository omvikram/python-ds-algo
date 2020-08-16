import heapq

## heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
## heappush – This function adds an element to the heap without altering the current heap.
## heappop - This function returns the smallest data element from the heap.
## heapreplace – This function replaces the smallest data element with a new value supplied in the function.


H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,8)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)