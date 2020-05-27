'''
Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary : 
    dic1={1:10, 2:20} 
    dic2={3:30, 4:40} 
    dic3={5:50,6:60}
Expected Result :
    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

dic1={1:10, 2:20} 
print('dic1: ', dic1)

dic2={3:30, 4:40} 
print('dic2: ', dic2)

dic3={5:50,6:60}
print('dic3: ', dic3)

new_dic = {}

print(' ')

#updating individually
print('----Updating Individually----')
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)

print('New_Dic: ', new_dic)

print(' ')

#using for loop
print('----Updating using for loop----')

new_dic2 = {}

for d in (dic1,dic2,dic3):
    new_dic2.update(d)

print('New_Dic: ',new_dic2)

