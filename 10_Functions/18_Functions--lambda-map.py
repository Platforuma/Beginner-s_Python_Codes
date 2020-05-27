#-----------normal------------
items = [1,2,3,4,5]
squared = []

for i in items:
    squared.append(i**2)

print(squared)
print(' ')

#-------------map---------------
items2 = [1,2,3,4,5]
squared2 = list(map(lambda x:x**2, items))
print(squared2)
print(' ')

#---------------normal-----------------

list3 = []
for i in range(5):
    list3.append(i*i)
    list3.append(i+i)
    print(list3)
    list3 = []

print(' ')

#---------------------map---------------
def multiply(x):
    return x*x

def add(x):
    return x+x

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x:x(i), funcs))
    print(value)
