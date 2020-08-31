# Implement a program, which given an integer n, computes the sum of its digits.
# If a negative number is given, the function should work as if it was positive.
# For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.
# In the test cases for this task we will have that -2^63 < n < 2^63.

# Test examples
# Input	Output
# 10	1
# 2	    2
# -3456	18
# 1325132435356	43

def digit_sum(number):
    sum = 0
    remainder = 0
    
    if(number > 0 and number < 10):
        return number
    elif(number < 0 or number >= 10):
        number = abs(number)
        while number > 0:
            remainder = number%10
            sum = sum + remainder
            number = number/10
            
    return sum

print(digit_sum(10))
print(digit_sum(11))
print(digit_sum(123))
print(digit_sum(-11))