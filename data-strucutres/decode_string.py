# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated 
# exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for 
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].

def decodeString(text):
    indexlist =[]
    characterlist =[]
    result = ""

    for ch in text:
        temp = ""
        if(str(ch).isdigit()):
            indexlist.append(int(ch))
        elif(ch == "]"):
            # print(indexlist)
            # print(characterlist)
            while(len(characterlist) != 0 and characterlist[-1] != "["):
                temp = characterlist.pop() + temp

            if(len(indexlist) != 0):
                index = indexlist.pop()
                result = result + (temp*index)
            characterlist.remove("[")
        else:
            characterlist.append(ch)
    
    print(indexlist)
    print(characterlist)
    print(result)

decodeString("3[a]2[bc]")
decodeString("3[a2[c]]")
decodeString("2[abc]3[cd]ef")
decodeString("abc3[cd]xyz")