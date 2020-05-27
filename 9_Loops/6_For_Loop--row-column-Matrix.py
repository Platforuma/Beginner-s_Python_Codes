'''
Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column
of the array should be i*j

Enter the number of row: 5
Enter the number of column: 3
11 , 12 , 13 , 14 , 15 , 

21 , 22 , 23 , 24 , 25 , 

31 , 32 , 33 , 34 , 35 , 
'''
#just printing in matrix format
print('----Making simple matrix----')
row = int(input('Enter the number of row: '))
column = int(input('Enter the number of column: '))

for i in range(1,row+1):
    for j in range(1,column+1):
        print(str(i)+str(j)+' ' , end =' ')
    print('\n')


print('')

#iterating list items
print('----Adding them to list items----')
item = []

for i in range(1,column+1):
    for j in range(1,row+1):
        item.append(str(i)+str(j))

print(item)

