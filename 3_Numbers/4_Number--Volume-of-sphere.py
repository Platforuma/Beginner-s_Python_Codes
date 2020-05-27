'''
Write a Python program to get the volume of a sphere with radius 6.
'''

#using general program
print('----using general program----')
radius = float(input('Enter the radius of Sphere: '))
volume = (4/3) * 3.14 * radius**3
print('Volume: ', str(volume))

#using math module
print('')
print('----using math module----')
import math
radius = float(input('Enter the radius of Sphere: '))
volume = (4/3) * math.pi * radius**3
print('Volume: ', str(volume))
