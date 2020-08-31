## Merge sort first divides the array into equal halves and then merge them in a sorted manner.
## After division, both partitions are unsorted but during the Merge process we compare each element 
## Compare and add smaller items on new list and remove it from the right/left partition list 
## Time Complexity - O(nlogn)

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    print(left_list)
    print(right_list)
    return list(mergeLists(left_list, right_list))

# Compare and Merge the sorted halves
def mergeLists(left_half,right_half):
    resultList = []
    
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            resultList.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            resultList.append(right_half[0])
            right_half.remove(right_half[0])
            
    if len(left_half) == 0:
        resultList = resultList + right_half
    else:
        resultList = resultList + left_half

    return resultList

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))