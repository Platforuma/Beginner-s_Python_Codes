'''
Write a python program which executes a for loop in a week days dictionary
and breaks it after Wednesday.
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']

for i in days:
    print(i)
    if i=='Wednesday':
        break
    
