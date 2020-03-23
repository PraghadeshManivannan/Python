a = []
b = [1,2]

#it checks whether the given element can be iterated or not
#all() allows empty list, tuple, set, dictionaries
print(all(a))
print(all(b))

#it checks whether the given element can be iterated or not
#any() does not allows empty list, tuple, set, dictionaries
print(any(a))
print(any(b))
