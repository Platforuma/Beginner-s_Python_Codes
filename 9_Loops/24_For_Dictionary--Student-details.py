'''
Write a Python program to print a dictionary in table format
'''

students = {'Lakhan':{'year': 2,
                   'branch':'mechanical'},
            'Roopika':{'year': 4,
                    'branch': 'computer science'}
            }

for a in students:
    print(a)
    for b in students[a]:
        print ('  ', b,':',students[a][b])
