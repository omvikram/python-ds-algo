
# Python program for Memoized version of nth Fibonacci number
# Top Down approach > using lookup table where we will save each sub results into the lookup table 
  
# Function to calculate nth Fibonacci number 
def fib(n, lookup): 
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
  
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
  
    # return the value corresponding to that value of n 
    return lookup[n] 
# end of function 
  
# Driver program to test the above function 
n = 34 
# Declaration of lookup table  
lookup = [None]*(n+1) 
print ("Fibonacci Number is ", fib(n, lookup)) 
  

# Python program Tabulated (bottom up) version 
# Bottum Up approach > In this approach we will calculate all the sub results and store it

# Function to calculate nth Fibonacci number 
def fib(n): 
  
    # array declaration 
    f = [0]*(n+1) 
  
    # base case assignment 
    f[1] = 1
  
    # calculating the fibonacci and storing the values 
    for i in xrange(2 , n+1): 
        f[i] = f[i-1] + f[i-2] 
    return f[n] 
  
# Driver program to test the above function 
print ("Fibonacci number is " , fib(9))