#built in functions
a = (1, 2, 3, 4.7, 56.3, 'a', 'b', 'cat')

#len
print('Length of a:', len(a))
print(' ')

#index
print('Index of "cat":', a.index('cat'))
print('Index of 4.7]:', a.index(4.7))
print('Index of "56.3":', a.index(56.3))
print(' ')

#max and min
b = (3,6,5,4,7,9,2,5,3,7)
print('maximum:', max(b))
print('minimum:', min(b))
print(' ')

#tuple and list
c = list(b)
print('List:', c)
c = tuple(c)
print('Tuple:', c)
