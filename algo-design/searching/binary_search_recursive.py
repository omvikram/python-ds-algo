## Binary Search using recursion
## Time Complexity O(nlogn) in a sorted list of items

def bsearch(list, start_index, end_index, val):

    if (end_index < start_index):
        return None
    else:
        midval = start_index + ((end_index - start_index) // 2)
        # Compare the search item value with middle indexed item value in a list
        # If less then mid value then search in the first half of the list
        # If greater then search in the second half of the list
        if list[midval] > val:
            return bsearch(list, start_index, midval-1,val)
        elif list[midval] < val:
            return bsearch(list, midval+1, end_index, val)
        else:
            return midval

my_list = [8,11,24,56,88,131]

# bsearch expects the list, start index, end index and the number to search
print(bsearch(my_list, 0, 5, 24))
print(bsearch(my_list, 0, 5, 51))