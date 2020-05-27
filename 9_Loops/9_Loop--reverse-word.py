'''
Write a Python program that accepts a word from the user and reverse it
'''

#usign simple method - Swati Amoniya
word=input("enter the word: ")
print("reverse of the word using Swati's method is", word[::-1])

#using list method
reverse = ''
for i in range(len(word)-1,-1,-1):
    reverse += ''.join(word[i])
print("reverse of the word using complex method is", reverse)

