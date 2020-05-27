#Dictionary operations

#creating
a = {'name':'Saral Jain',
     'age':23,
     'instructor':['iot','Python','JavaScript'],
     'position':'Founder'}
print(a)
print(' ')

#accessing
print('Position:', a['position'])
#print(a['language'])
print(' ')

#updating
print(a)
a['position'] = 'Director'
a['language'] = 'Python'
print(a)
print(' ')

#deleting
del(a['position'])
print(a)
print(' ')


