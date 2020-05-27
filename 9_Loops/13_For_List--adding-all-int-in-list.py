'''
Write a Python program to sum all the items in a list
'''

num = input('Enter the list numbers: ')
num = num.split('+')
result = 0
for i in num:
    result = result + int(i)

print('Sum of all the list item: ', str(result))
