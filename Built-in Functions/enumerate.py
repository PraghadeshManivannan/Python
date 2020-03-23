#returns the enumerate object
#iterable will be the sequence
#it gives the tuples with the number along with the sequence
#enumerate(sequence)#it takes the starting value as 0
#staring value can be intialized as we wish using enumerate(sequence,start = 1)

a = [1,2,3]

b = list(enumerate(a,start = 1))

print(b)
