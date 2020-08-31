# Write a function which accepts two parameters - the number N and a list in which it must store the filenames
#  in the correct sorted order. Look at the boilerplate code for your favorite language.

def sort_the_files(n, result=[]):
    for i in range(1,n+1):
        result.append("IMG" + str(i) + ".jpg")
    
    # Python uses Timsort in its sort() method. 
    # It is a hybrid sorting algorithm that uses both "Merge sort and Insertion sort" techniques.
    result.sort() 
    return result

print(sort_the_files(15))



