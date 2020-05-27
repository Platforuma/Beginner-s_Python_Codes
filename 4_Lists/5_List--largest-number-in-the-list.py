'''
Write a Python program to get the largest number from a list
'''

num = input('Enter all the numbers: ')
num = num.split(',')
num.sort()
print('The largest number in the list is: ', str(num[-1]))
