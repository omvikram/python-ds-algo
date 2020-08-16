## It is a comparison-based algorithm in which each pair of adjacent elements is compared and 
## the elements are swapped if they are not in order.

def bubble_sort(list):
    list_length = len(list)
    for i in range(list_length - 1, 0, -1):
        for j in range(i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            

list = [19,2,31,45,6,11,121,27]
bubble_sort(list)
print(list)