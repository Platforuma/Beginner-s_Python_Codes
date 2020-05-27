'''
Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:
Input a letter of the alphabet: k                                       
k is a consonant.
'''

letter = input('Input a letter of the alphabet: ')

if letter in 'aeiouAEIOU':
    print(letter, ' is a vowel')
else:
    print(letter, ' is a consonant')
