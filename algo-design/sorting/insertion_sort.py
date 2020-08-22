## Function to perform Insertion sort 
## Take the min value in the list and then try to insert it in the best possible location
## Divide the list in Sorted and Unsorted list items and pick the 2nd element as marker 
## Now you will have left side as Sorted list while Right side of the elements as Unsorted list
## Start traversing from 1st item to the Rightmost and check on Left sorted items to compare
## If Left item is < current marker swap and proceed to the Rightmost item 
## Time Complexity O(n**2)

def insertionSort(mylist):
   #Here the 1st index or 2nd element is marker
   for index in range(1,len(mylist)):
     marker = mylist[index]
     leftIndex = index

     while leftIndex > 0 and mylist[leftIndex-1] > marker:
         mylist[leftIndex] = mylist[leftIndex-1]
         leftIndex = leftIndex-1

     mylist[leftIndex]=marker
     print(mylist)

mylist = [14,46,43,27,57,41,45,21,70]
insertionSort(mylist)