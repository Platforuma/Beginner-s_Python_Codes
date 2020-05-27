'''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
#prompt
color = input('Enter the colors: ')

#string to list conversion
color_list = color.split(',')
print('All color list: ', color_list)
print('First color of list: ', color_list[0])
print('Last color of list: ', color_list[-1])
