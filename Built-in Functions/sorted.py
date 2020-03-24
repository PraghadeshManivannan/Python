
#sorted(iterable, /, *, key=None, reverse=False)
#Return a new list containing all items from the iterable in ascending order.
'''A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.'''


a = [1,4,6,8,0,2,3,7,9,5]
print(sorted(a))
print(sorted(a,reverse = True))
