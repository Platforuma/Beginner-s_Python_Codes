'''
Write a Python program to print out a set containing all the colors from color_list_1
which are not present in color_list_2.
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}
'''

#using normal list 
print('----Using list method----')
color_list_1 = ["White", "Black", "Red"] 
color_list_2 = ["Red", "Green"]
new_set = []
for x in color_list_1:
    if x not in color_list_2:
        new_set += [x]
print(new_set)


#using set methods
print(' ')
print('----Using set method----')
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))
