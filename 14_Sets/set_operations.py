#Operations in set
#with methods and operators

##union
a = {'a','b','c','d'}
b = {1, 2, 3, 4, 5}
c = a | b
print('c: ', c)
d = a.union(b)
print('d: ', d)

#different types can be unioned with set using union
#multiple unions are also valid in sets
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.union(b, c, d))
print(a | b | c | d)

##intersection
a = {'a', 'b', 'cat'}
b = {'cat', 'dog', 'e'}

print(a.intersection(b))
print(a & b)

#multiple intersection
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.intersection(b, c, d))
print(a & b & c & d)

##difference: return the set of all elements that are in a but not in b:
a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}

print(a.difference(b))

print(a - b)

#muliple difference
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

print(a.difference(b, c))
print(a - b - c)

##symetric_difference
a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}

print(a.symmetric_difference(b))
print(a ^ b)

#multiple symetric_difference only with operator

a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}

print(a ^ b ^ c)

##disjoint
a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}

print(a.isdisjoint(b))
b = b - {'c'}
print(a.isdisjoint(b))

##issubset
a = {'a', 'b', 'c'}
b = {'a', 'b', 'c', 'd', 'e'}
a.issubset(b)

c = {'a', 'b', 'c'}
print(a <= c)

##issuperset
a = {'foo', 'bar', 'baz'}
b = {'foo', 'bar'}
print(a.issuperset(b))

c = {'baz', 'qux', 'quux'}
print(a >= c)

##updating a set
a = {'foo', 'bar', 'baz'}
b = {'foo', 'baz', 'qux'}

#union update
a |= b
print(a)
a.update(['corge', 'garply'])
print(a)

#insertion update
a = {'a', 'b', 'c'}
b = {'a', 'c', 'd'}

a &= b
print(a)

a.intersection_update(['c', 'd'])
print(a)

#difference update
a = {'a', 'b', 'c'}
b = {'a', 'c', 'd'}

a -= b
print(a)

a.difference_update(['a', 'b', 'd'])
print(b)


#symmetric_difference_update
a = {'a', 'b', 'c'}
b = {'a', 'c', 'd'}

a ^= b
print(a)

a.symmetric_difference_update(['d', 'e'])
print(a)




