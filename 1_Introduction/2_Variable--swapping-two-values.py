'''
Write a Python program to swap two variables
'''
#using temporary variable
print('----Using temp variable----')
x = input('Enter first variable: ')
y = input('Enter second variable: ')
z = x
x = y
y = z
print('Value of first variable now is: ', x)
print('Value of second variable  now is: ', y)

print(' ')
#using same variables
print('----swaping variable----')
x = input('Enter first variable: ')
y = input('Enter second variable: ')
x, y = y, x
print('Value of first variable now is: ', x)
print('Value of second variable  now is: ', y)
