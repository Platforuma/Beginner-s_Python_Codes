'''
Write a Python program that accepts a string and calculate the number of
digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
'''

string = input("Enter a string: ")

digit = length = 0

for char in string:
    if char.isdigit():
        digit = digit + 1
    elif char.isalpha():
        length = length + 1
    else:
        pass
    
print("Letters in String: ", length)
print("Digits in String: ", digit)
