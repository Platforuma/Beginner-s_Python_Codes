'''
Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output : 
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def letter_counter(text):
    l_case = 0
    u_case = 0
    numbers = 0
    
    for letter in text:
        if letter.islower():
            l_case += 1
        elif letter.isupper():
            u_case += 1
        elif letter.isdigit():
            numbers += 1

    return 'Lower Cas: ', l_case, 'Upper Case: ', u_case, 'Numbers: ', numbers

print(letter_counter('The quick Brow Fox'))
print(letter_counter('TTTTTis5times'))

