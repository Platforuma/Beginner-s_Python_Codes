'''
Write a Python function to sum all the numbers in a list
'''

def sum_of_numbers(list_num):
    result = 0
    for i in list_num:
        result = i + result
    return result

print(sum_of_numbers((2,3,5,6,8,9)))
print(sum_of_numbers((0,1,2,3,4,5,6,7,8,9)))
print(sum_of_numbers([1,2,3]))
print(sum_of_numbers([180,200,360,98,54,2]))
print(sum_of_numbers([56.6,883.3,66.2]))
