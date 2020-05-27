'''
Define a function that can accept two strings as input and
print the string with maximum length in console.
If two strings have the same length, then the function
should print al l strings line by line
'''

def max_len(string1, string2):
    len_str_1 = len(string1)
    len_str_2 = len(string2)

    if len_str_1 > len_str_2:
        return string1
    elif len_str_2 > len_str_1:
        return string2
    else:
        return string1, string2

print(max_len('Platforuma', 'Python'))
print(max_len('Python', 'Platforuma'))
print(max_len('Platforuma','Platforuma'))
