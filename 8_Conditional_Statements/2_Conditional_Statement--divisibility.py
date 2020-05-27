'''
Write a Python function to check whether a number is divisible by
another number. Accept two integer’s values form the user
'''

dividend = int(input('Enter the dividend: '))
divisor = int(input('Enter the divisor: '))

if dividend%divisor==0:
    print('Divisible')
else:
    print('Not Divisible')
