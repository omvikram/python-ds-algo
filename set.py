# set initialization by passing in a list
myset = set([1,2,3,3,3])

# set initialization using {}
myset = {1,2,3,3,3}

# iteration of set
for ele in myset:
  print(ele)

# check if ele in set:
print(True if ele in myset else False)

# add an element to set:
myset.add(ele)

# remove an element from set
myset.remove(ele)

# get length of the set
print(len(myset))


myset1 = {1,2,3}
myset2 = {1,2,4,5}

# union
myset = myset1.union(myset2)

# intersection
myset = myset1.intersection(myset2)

# difference
myset = myset1.difference(myset2)