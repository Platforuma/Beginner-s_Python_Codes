'''
Write a python program which executes a for loop in a week days dictionary
and continues it after Wednesday.
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']

for i in days:
    if i=='Wednesday':
        continue
    print(i)    
