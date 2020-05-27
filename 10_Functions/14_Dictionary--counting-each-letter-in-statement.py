'''
Write a Python program to count the number of each character of a given text of a statement
'''

statement = '''The quick brown fox jumps over the lazy dog. The fox was brown and the dog was lazy.
one used to jump and the other one used to lay and just sleep. Although these staements do not make any
sense but they are important this exercise. So just keep typing untill we have at least four to five lines.
'''

def char_counter(string):
    count = {}
    for char in string:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1
    print(count)

print(statement)
char_counter(statement)

print(' ')

print('google.com')
char_counter('google.com')
