'''
Write a Python program to multiplies all the items in a list
'''
num = input('Enter the list numbers: ')
num = num.split(',')
result = 1
for i in num:
    result = result * int(i)

print('Product of all the list item: ', str(result))
