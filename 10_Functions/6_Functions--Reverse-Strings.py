'''
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321" 
'''
#using string index method
print('----String Index Method----')

def r_string(fstring):
    
    rstring = ''
    index = len(fstring)    
    while index>0:
        rstring += fstring[ index - 1 ]
        index = index - 1
    return 'Original: ', fstring, 'Reverse: ', rstring

print(r_string('1234abcd'))
print(r_string('Platforuma'))
print(r_string('Python'))
print(r_string('Arduino'))
print(r_string('Indore'))
print(r_string('Iron Man'))

print(' ')

#using list reverse method
print('----List Index Method----')

def reverse_string(text):
    flip = []
    for i in range(len(text)-1,-1,-1):
        flip.append(text[i])
    
    strings = ''
    for letters in flip:
        strings += str(letters)
    print('Straight Order: ', text,', Reverse Order: ', strings )

reverse_string('1234abcd')
reverse_string('Platforuma')
reverse_string('Python')
reverse_string('Arduino')
reverse_string('Indore')
reverse_string('Iron Man')
