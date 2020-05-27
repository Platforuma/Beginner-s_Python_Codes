'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

vowels = 'aeiouAEIOU'

letter = input('Enter a letter: ')

if letter in vowels:
    print("It is a vowel")
else:
    print('It is not a vowel')
