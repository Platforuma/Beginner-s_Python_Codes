'''
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java 
Output : java
'''

filename = input('Enter the file name: ')
filename = filename.split('.')
print('Extension: ', filename[1])

