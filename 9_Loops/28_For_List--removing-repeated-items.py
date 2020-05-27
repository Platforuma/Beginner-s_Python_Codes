'''
Write a Python program to remove duplicates from a list
'''

list_items = input('Enter the list items: ')
list_items = list_items.split(',')


new_list = []

for items in list_items:
    if items not in new_list:
        new_list.append(items)

print(new_list)
