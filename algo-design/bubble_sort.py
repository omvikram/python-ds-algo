## It is a comparison-based algorithm in which each pair of adjacent elements is compared and 
## the elements are swapped if they are not in order. There are 2 loops in this algo 
## one which goes reverse order (i) and another in forward order (j), 
## if item[j] is greater than item[j+1] swap the items

def bubble_sort(list):
    list_length = len(list)
    for i in range(list_length - 1, 0, -1):
        for j in range(i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        print(list)   

list = [19,2,31,45,6,11,121,27]
bubble_sort(list)