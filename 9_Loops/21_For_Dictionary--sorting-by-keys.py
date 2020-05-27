'''
Write a Python program to sort a dictionary by key
'''

dic = {'India': 'Delhi',
       'Nepal': 'Kathmandu',
       'Japan': 'Tokyo',
       'China': 'Beijing',
       'England': 'London'}

print(dic)
for i in sorted(dic):
    print("%s: %s" %(i, dic[i]))
