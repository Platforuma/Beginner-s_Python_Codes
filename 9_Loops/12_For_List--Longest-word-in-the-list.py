'''
Write a Python function that takes a list of words and returns the length of the longest one
'''

word_list = input("Enter the word list with ',': ")
word_list = word_list.split(',')

length = []

for words in word_list:
    length.append(len(words))

length.sort()
print('Longest letter in the list with a lengthe of: ', str(length[-1]))

word_list_2 = input("Using max method:")
word_list_2 = word_list_2.split(',')
length_2 = []
for words_2 in word_list_2:
    length_2.append(len(words_2))

print('Longest letter in the list with a lengthe of: ', str(max(length_2)))
