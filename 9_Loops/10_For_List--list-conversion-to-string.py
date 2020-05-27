'''
Write a Python program to concatenate all elements in a list into a
string and return it.
'''
a = input('ENter the words')
list_of_words = a.split(',')
strings = ''
print(list_of_words)
for letters in list_of_words:
    strings += str(letters)

print(strings)
    
