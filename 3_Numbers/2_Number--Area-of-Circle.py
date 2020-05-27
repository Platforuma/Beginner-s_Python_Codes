'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output : r = 1.1
Area = 3.8013271108436504
'''

#using general program
print('----using general program----')
radius = float(input('Enter the radius: '))
area = 3.14 * radius**2
print('Area: ' + str(area))

#using math module
print('')
print('----using math module----')
import math
radius = float(input('Enter the radius: '))
area = math.pi * radius**2
print('Area: ' + str(area))
