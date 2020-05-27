'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary. 
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output: 
ac
ad
bc
bd
'''

dic = {'1':['a','b'], '2':['c','d']}

d = []

for values in dic.values():
    d.append(values)

print(d)
print(d[0][0] + d[0][1])
print(d[0][1] + d[1][0])
print(d[0][0] + d[1][0])
print(d[1][0] + d[1][1])
print(d[0][0] + d[1][1])
    
