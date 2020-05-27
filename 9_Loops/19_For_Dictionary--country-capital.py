'''
Write a Python program to map two lists into a dictionary
'''

country = ['India', 'Nepal', 'Japan', 'China', 'England']
capital = ['Delhi', 'Kathmandu', 'Tokyo', 'Beijing', 'London']

new_dic = {}


#using Dictionary Methods
print('----Dictionary Method----')
new_dic = dict(zip(country, capital))
print(new_dic)

print(' ')

#using for loop and zip
print('----For Loop and Zip----')

new_dic2 = {}
for i,j in zip(country, capital):
    new_dic2[i] = j

print(new_dic2)
