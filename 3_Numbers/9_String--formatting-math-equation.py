'''
Given variables x=30 and y=20,
write a Python program to print t "30+20=50"
'''

x = int(input('Enter x: '))
y = int(input('Enter y: '))
result = x + y

print(' ')
print('---using % operator----')
print('%d + %d = %d' % (x, y, result))

print(' ')
print('----using format----')
print('{0} + {1} = {2}'.format(x, y, result))
