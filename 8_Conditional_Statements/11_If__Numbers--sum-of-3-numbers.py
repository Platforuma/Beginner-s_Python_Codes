'''
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum.
'''

first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))

if first_num==second_num==third_num:
    sum = first_num + second_num + third_num
    sum = sum * 3
    print('All nums are equal, hence thrice the sum is: ', str(sum))

else:
    sum = first_num + second_num + third_num
    print('Sum of three number: ', str(sum))    
