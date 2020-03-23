#id(obj, /)
#Return the identity of an object.
#This is guaranteed to be unique among simultaneously existing objects.
#(CPython uses the object's memory address.)'''


a = [1,2,3]
b = a
print(id(a))
print(id(b))
