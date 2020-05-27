'''
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

new_dic = {}

for i in d1.keys():
    for j in d2.keys():
        if i == j:
            v = d1[i] + d2[j]
            new_dic[i] += v
        else:
            new_dic[j] = [j]

print(new_dic)
