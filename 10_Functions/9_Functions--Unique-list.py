'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_items(item_list):
    unique_list = []
    for i in item_list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

unique_items((1,2,3,3,3,3,4,5))
