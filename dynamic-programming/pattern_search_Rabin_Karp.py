## Robin Karp Pattern Search works on the Hash Creation
## It works on the theory that if the 2 strings are equal then their hash will also be equal
## Time Complexity O(mn) where m and n are the length of the test and pattern respec. 

txt = input("please enter the test string :")
pat = input("please enter the pattern to search :")

count = 0
x = len(txt)
y = len(pat)

pat_hash = str(hash(pat))

# Traverse through each word starting from i = 0 equal to the length
# This will work only if the exact word is present in the sentence
for i in range(0, x-y+1):
    substr = txt[i:i+y]
    substr_hash = str(hash(substr))
    
    if(pat_hash == substr_hash):
        count = count + 1
        
print(count)