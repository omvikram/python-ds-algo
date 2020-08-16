# Function to do insertion sort 
def insertionSort(mylist): 
    for i in range(1, len(mylist)): 
        key = mylist[i] 
        print(key)
        j = i-1
        while j >= 0 and key < mylist[j] : 
                mylist[j + 1] = mylist[j] 
                j = j - 1
        mylist[j + 1] = key
        print(mylist)

mylist = [12, 11, 13, 5, 6] 
insertionSort(mylist)