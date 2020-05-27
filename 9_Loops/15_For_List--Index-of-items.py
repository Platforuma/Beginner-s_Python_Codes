'''
Write a Python program access the index of a list.
'''

list_items = input('Enter the list items: ')
list_items = list_items.split(',')
for i in range(0,len(list_items)):
    print('Index of ' + list_items[i] + ' is ' + str(i)) 
