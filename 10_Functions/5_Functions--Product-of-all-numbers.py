'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336  
'''
##def product_of_numbers(list_num):
##    result = 1
##    for i in list_num:
##        result = i * result
##    return result
##
##print(product_of_numbers((7,6,2)))
##print(product_of_numbers((0,1,2,3,4,5,6,7,8,9)))
##print(product_of_numbers([1,2,3]))
##print(product_of_numbers([1000,2100,3000,.0003]))
##print(product_of_numbers([56.6,883.3,66.2]))
##print(product_of_numbers((8, 2, 3, -1, 7)))



def product_of_numbers(*num):
    result = 1
    for i in num:
        result = i + result
    return result

print(product_of_numbers(1,2,3,4,5,6,7,8,9))
