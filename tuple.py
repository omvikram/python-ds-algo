x_tuple = ()
y_tuple = ()
print("Tuples are initialised")

mylist = [1,2,3]
x_tuple = 1,2,3,4,5
y_tuple = ('c','a','k','e')

print(x_tuple[0])
#x_tuple[0] = 0 cannnot assign the value in a tuple

list_tuple = tuple(mylist)
print(list_tuple)

z_tuple = x_tuple + y_tuple
print(z_tuple)

nested_tuple = (list_tuple, z_tuple)
print(nested_tuple)

print(list_tuple*2)

#finally you can delete a tuple also