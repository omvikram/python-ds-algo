## Binary Search using divide and conquer algo
## Time Complexity O(nlogn) in a sorted list of items

def bsearch(list, val):

    list_size = len(list) - 1

    start_index = 0
    end_index = list_size
    
    # Find the middle most value
    while(start_index <= end_index):
        midval = (start_index + end_index)//2

        if list[midval] == val:
            return midval
        # Compare the search item value with middle indexed item value in a list
        # If less then mid value then search in the first half of the list
        # If greater then search in the second half of the list
        if val > list[midval]:
            start_index = midval + 1
        else:
            end_index = midval - 1

    if start_index > end_index:
        return None


# Initialize the sorted list
list = [2,7,19,34,53,72]

# Print the search result
print(bsearch(list,72))
print(bsearch(list,11))