# A palindrome is а word or a phrase or a number, that when reversed, stays the same.
# For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

# But this time, we are not interested in words but numbers. A "number palindrome" is a number, 
# that taken backwards, remains the same.

# For example, the numbers 1, 4224, 9999, 1221 are number palindromes.
# Implement a function, which given an integer computes if it's a palindrome.

# Input
# One integer n, where 0 < n <= 10,000,000,000.

# Output
# Your function must return a boolean true if n is a palindrome and false otherwise.

# Test examples
# Input	Output
# 1	true
# 42	false
# 100001	true
# 999	true
# 123	false

def is_numeric_palindrome(num):
    # Store each number in List
    is_palindrome = False
    if(num > 0 and num < 10):
        is_palindrome = True
        return is_palindrome
    if(num > 10):
        mylist = []
        for each in str(num):
            mylist.append(int(each))
    
    # Compare the first and last number in List till mid index
    length = len(mylist)
    midlength = int(length/2)
    for i in range(0, midlength):
        if(mylist[i] == mylist[length-i-1]):
            is_palindrome = True
        else:
            is_palindrome = False
            break
    return is_palindrome

print(is_numeric_palindrome(1))
print(is_numeric_palindrome(42))
print(is_numeric_palindrome(100001))
print(is_numeric_palindrome(999))
print(is_numeric_palindrome(123))
