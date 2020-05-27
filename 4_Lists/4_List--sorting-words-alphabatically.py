'''
Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
	without,hello,bag,world
Then, the output should be:
	bag,hello,without,world
'''

list_item = input("Enter the list item separated with ',': ")
list_item = list_item.split(',')
list_item.sort()
print("Sorted List Items: ", list_item)
print('Word Sequence: ', ', '.join(list_item))


