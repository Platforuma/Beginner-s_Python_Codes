#built in functions
a = [1, 2, 3, 4.7, 56.3, 'a', 'b', 'cat']

#len
print(len(a))
print(' ')

#append
print(a)
a.append('dog')
print(a)
a.append(['elephant', 'fish'])
print(a)
print(' ')

#extend
a.extend(['gun','hen'])
print(a)
print(' ')

#insert
a.insert(3,'fourth')
print(a)
print(' ')

#index
print('Index of "fourth":', a.index('fourth'))
print('Index of "[\'elephant\', \' fish\']":', a.index(['elephant', 'fish']))
print('Index of "56.3":', a.index(56.3))
print(' ')

#pop
print(a)
print('poped element:', a.pop())
print(a)
print(' ')

#remove
print(a)
a.remove(['elephant','fish'])
print(a)
print(' ')

#reverse
print(a)
a.reverse()
print(a)
print(' ')

#sort
b = [4,6,3,2,3,3,4,8,9,2,1,6]
c = ['a', 'm', 'r', 'd', 'z', 'e', 'f', 'h']
a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)
