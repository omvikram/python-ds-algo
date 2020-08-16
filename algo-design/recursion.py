## Binary Search using recursion

def bsearch(list, start_index, end_index, val):

    if (end_index < start_index):
        return None
    else:
        midval = start_index + ((end_index - start_index) // 2)

# Compare the search item with middle most value

        if list[midval] > val:
            return bsearch(list, start_index, midval-1,val)
        elif list[midval] < val:
            return bsearch(list, midval+1, end_index, val)
        else:
            return midval

my_list = [8,11,24,56,88,131]

print(bsearch(my_list, 0, 5, 24))
print(bsearch(my_list, 0, 5, 51))