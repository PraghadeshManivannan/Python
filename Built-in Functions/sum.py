
#sum(iterable, start=0, /)
#Return the sum of a 'start' value (default: 0) plus an iterable of numbers
#When the iterable is empty, return the start value.
'''This function is intended specifically for use with numeric values and may
reject non-numeric types.'''



a = [1,3,5,7,9,4,6,2,8]

print(sum(a))
print(sum(a,start = 4))
