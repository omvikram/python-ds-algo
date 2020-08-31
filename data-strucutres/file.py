# File modes (2nd argument): 'r'(read), 'w'(write), 'a'(appending), 'r+'(both reading and writing)

try:

    f = open('file_name', 'w') #in python or python2
    f = open('file_name') #in python3

    # Reads entire file
    f.read() 

    # Reads one line at a time
    f.readline() 

    # Writes the string to the file, returning the number of char written
    f.write('Add this line.') 

except:
    # handle exception here 

finally:
    f.close()