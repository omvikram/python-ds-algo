x =[]
print(type(x))

x = [1,2,3]
print(type(x))

x.append(4)
print(x)

x.insert(-1,5)
print(x)
print(x[-1])

x.remove(4)
print(x)

x[-1] = 4
print(x)

mylist = ['c', 'o', 'k', 'i', 'e']
mylist.pop(-2)
print(mylist)

mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)
