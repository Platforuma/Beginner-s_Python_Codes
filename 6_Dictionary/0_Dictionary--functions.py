#Dict Functions

a = {'name':'Saral Jain',
     'age':23,
     'instructor':['IoT','Python','JavaScript'],
     'position':'Founder'}
print(a)
print(' ')

#len
print('Length of a:', len(a))
print(' ')

#copy
b = a.copy()
print('values of b:', b)
print(' ')

#get
print('Instructor of:', a.get('instructor'))
print(' ')

#items
print(a.items())
print(' ')

for i in a.items():
    print(i)
print(' ')

#keys
print(a.keys())
print(' ')

#values
print(a.values())
print(' ')

#updates
c = {'a':1, 'b':2, 'c':3}
d = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}

print('old:', c)
c.update(d)
print('new:', c)

