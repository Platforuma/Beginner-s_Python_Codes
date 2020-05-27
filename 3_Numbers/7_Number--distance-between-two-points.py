'''
Write a Python program to compute the distance between the points
(x1, y1) and (x2, y2)
'''

#simple method
print('----Input x1, y1, x2, y2 Seperately----')
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print('Disance: ', str(distance))


print(' ')

#using (x1,y1) and (x2,y2) initially and splitting them as a list
print('----Input (x1,y1) & (x2,y2) as Coordinates----')
first_point = input(r'Enter (x1,y1): ')
first_point = first_point.split(',')

second_point = input(r'Enter (x2,y2): ')
second_point = second_point.split(',')

distance = ((int(second_point[0])-int(first_point[0]))**2 + (int(second_point[1])-int(first_point[1]))**2)**(1/2)
print('Distance: ', str(distance))


