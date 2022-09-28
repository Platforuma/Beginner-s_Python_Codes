##add element to set
a = {'a', 'b', 'c'}

a.add('d')
print(a)

##remove element from set
a = {'a', 'b', 'c'}

a.remove('b')
print(a)


##discard: doesnot raise any exception
a = {'a', 'b', 'c'}

a.discard('b')
print(a)

a.discard('d')
print(a)

##pop: removes random element from set
a = {'a', 'b', 'c'}

a.pop()
print(a)

a.pop()
print(a)

a.pop()
print(a)

#clear: clears the set
a = {'a', 'b', 'c'}

print(a)
a.clear()
print(a)
