# Input is read from the standard input. On the first line will be the word W. 
# On the second line will be the text to search.

# The result is written to the standard output. It must consist of one integer - 
# the number of occurrences of W in the text including the typos as defined above.

# SAMPLE INPUT

# banana
# there are three bananas on the tree and one banano on the ground
# SAMPLE OUTPUT

# 2

def findTyposCount():
    txt = input("Please enter the searching text here:")
    pat = input("Please enter the searchable pattern here:")

    pat_len = len(pat)
    txt_arr = txt.split(" ")
    counter_list = []

    for each in txt_arr:
        counter = 0
        txt_len = len(each)
        if(txt_len >= pat_len):
            ## Call a function to check the max possible match between each text and pattern
            ## If matching count > 1 then we can consider it as typo (ideally matching count > pat_len/2)
            counter_list.append(each)
                        
    print(counter_list)

findTyposCount()
