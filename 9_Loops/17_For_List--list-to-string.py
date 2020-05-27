'''
Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
'''

list_num = input('Enter the numbers: ')
list_num = list_num.split(',')
print('List: ', str(list_num))

single = ''

for num in list_num:
    single = single + num

single = int(single)
print(single)
