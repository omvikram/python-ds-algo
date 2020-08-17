# importing "array" for array creations but in Python mostly list replace the array
import array 
  
# creating an array with integer type 
myarr1 = array.array('i', [1, 2, 3]) 
  
# printing original array 
print ("The new created array is : ") 
for i in myarr1: 
    print (myarr1[i]) 
print() 
  
# creating an array with float type 
myarr2 = array.array('f', [2.5, 3.2, 3.3]) 
  
# printing original array 
print ("The new created array is : ") 
for i in myarr2: 
    print (myarr2[i]) 


#insert an element in the array 
myarr1.insert(1,4)

#append an element in the array
myarr2.append(4.4)

#access any element in an array
print(myarr1[1])
print(myarr2[2])

# using index() to print index of 1st occurrenece of 2 
print(myarr1.index(2)) 
  
# using index() to print index of 1st occurrenece of 1 
print(myarr1.index(1)) 

# using remove() to remove 1st occurrence of 1 
myarr1.remove(1) 

# using pop() to remove element at 2nd position 
myarr2.pop(2)

# updating a element in a array 
myarr1[2] = 6

# updating a element in a array 
myarr2[2] = 2.5