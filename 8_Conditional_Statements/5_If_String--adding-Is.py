'''
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
'''

string = input('Enter a string: ')

if string[0]=='I' and string[1]=='s':
    print(string)
else:
    print('Is' + string)
