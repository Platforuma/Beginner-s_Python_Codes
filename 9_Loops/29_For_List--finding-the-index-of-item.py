'''
Write a Python program to find the index of an item in a specified list
'''

list_items = input('Enter the list items: ')
list_items = list_items.split(',')

item = input('Enter the item for index: ')

for i in range(0, len(list_items)):
    if list_items[i] == item:
        print('Index of ' + item + ' is ' + str(i))
        
