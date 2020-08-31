# Function to get no of bits in binary representation of positive integer 
def countBits(n): 
	count = 0
	# using right shift operator
	while (n): 
		count += 1
		n >>= 1
		
	return count 

# Driver program 
i = 65
print(countBits(i)) 

##########################################################################

# Python3 program to find total bit in given number 
import math 
def countBitsByLog(number): 
	
	# log function in base 2 take only integer part 
	return int((math.log(number) / math.log(2)) + 1); 

# Driver Code 
num = 65; 
print(countBitsByLog(num)); 
