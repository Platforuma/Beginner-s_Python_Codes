#zip
a = ['saral','pradeep','somil','shreyash']
b = ['python','embedded c','Photoshop','c/c++']
c = [23,22,23,23]

d = zip(a,b,c)
print(d)
print(' ')

e = tuple(zip(a,b,c))
print(e)
print(' ')

for i in zip(a,b,c):
    print(i)
print(' ')

f = {}
for k,v in zip(a,b):
    f[k] = v

print(f)
