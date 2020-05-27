'''
Write a Python program to get the third side of
right angled triangle from two given sides
'''
print("For the unknown value enter 'x'")

h = input('Enter the Hypotaneous: ')
p = input('Enter the Perpendicular: ')
b = input('Enter the Base: ')

if h=='x':
    h = (float(p)**2 + float(b)**2)**(1/2)
    print('Hypotaneous (h): ', str(h))

elif p=='x':
    p = (float(h)**2 - float(b)**2)**(1/2)
    print('Perpendicular (p): ', str(p))

elif b=='x':
    b = (float(h)**2 - float(p)**2)**(1/2)
    print('Base (b): ', str(b))

else:
    print('Invalid format. One value must be x')
