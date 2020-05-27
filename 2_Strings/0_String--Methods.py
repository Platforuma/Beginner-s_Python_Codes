#String

a = 'Platforuma'
b = 'saral'
c = 'PYTHON'

#count: returns int. Gives the number of count of the element.
print('Count of "a" in Platforuma: ', a.count('a'))
print('Count of "a" in saral: ', b.count('a'))
print('Count of "S" in saral: ', b.count('S'))
print('Count of "s" in saral: ', b.count('s'))
print('Count of "a" in PYTHON: ', c.count('a'))
print(' ')

#islower: returns boolean(True), if all are lower case
print('Platforuma: ', a.islower())
print('saral: ', b.islower())
print('PYTHON: ', c.islower())
print(' ')

#isupper returns boolean(True), if all are Upper case
print('Platforuma: ', a.isupper())
print('saral: ', b.isupper())
print('PYTHON: ', c.isupper())
print(' ')

#len: reutrns int. Gives total number of elements
print('Platforuma: ', len(a))
print('saral: ', len(b))
print('PYTHON: ', len(c))
print(' ')

#lower: reurns String. Converts all the case to lower
print('Platforuma: ', a.lower(), a)
print('saral: ', b.lower(), b)
print('PYTHON: ', c.lower(), c)
print(' ')

#upper: reurns String. Converts all the case to upper
print('Platforuma: ', a.upper(), a)
print('saral: ', b.upper(), b)
print('PYTHON: ', c.upper(), c)
print(' ')

#replace: returns string. replaces a value with given value.
print('Platforuma: ', a.replace('a', 'XXX'), a)
print('saral: ', b.replace('a', 'XXX'), b)
print('PYTHON: ', c.replace('a', 'XXX'), c)
print(' ')

#index: reuturns int. gives index of the element
print('Platforuma: ', a.index('f'))
print('saral: ', b.index('a'))
#print('PYTHON: ', c.index('a')) -- raises an error
print(' ')


#split - converts to list elements
d = 'The quick bron fox jumps over the lazy dog'
e = 'Saral-Jain-Python-1996'
print(d.split(' '))
print(e.split('-'))
