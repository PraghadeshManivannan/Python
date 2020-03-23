#pow(x, y, z=None, /)
#Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
'''Some types, such as ints, are able to use a more efficient algorithm when
 invoked using the three argument form.'''

#if three arguements x,y,z is passed it will return ((x**y)%z)


print(pow(9,2))
print(pow(9,2,8))
