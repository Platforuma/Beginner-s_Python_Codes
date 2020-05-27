'''
Write a Python program to calculate midpoints of a line.
'''

#simple method
print('----Input x1, y1, x2, y2 Seperately (%)----')
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
mid_x = (x2+x1)/2
mid_y = (y2+y1)/2
print('Mid point: (%f, %f)' % (mid_x, mid_y))


print(' ')

#using (x1,y1) and (x2,y2) initially and splitting them as a list
print('----Input (x1,y1) & (x2,y2) as Coordinates (format)----')
first_point = input(r'Enter (x1,y1): ')
first_point = first_point.split(',')

second_point = input(r'Enter (x2,y2): ')
second_point = second_point.split(',')

mid_x = (x2+x1)/2
mid_y = (y2+y1)/2
print('Mid point: ({0}, {1})'.format(mid_x, mid_y))

