'''
Write a Python program to find the median among three given numbers
'''
#using general method
print('----General Method - Comparing each value----')
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)

print(' ' )

#using list method
print('----Using simple list method----')
numbers = input("Enter the 3 numbers sperated by ',': ")
numbers = numbers.split(',')
numbers.sort()
print('Median: ', numbers[1])
