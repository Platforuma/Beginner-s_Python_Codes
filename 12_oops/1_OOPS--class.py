'''
Python Class
'''
class DemoClass: #CamelCasing
    pass

obj1 = DemoClass()
print(obj1)
print(type(obj1))
print(id(obj1))
print(' ')

obj2 = DemoClass()
print(obj2)
print(type(obj2))
print(id(obj2))
print(' ')

obj3 = obj1
print(obj3)
print(type(obj3))
print(id(obj3))

print(dir(DemoClass))
print(' ')

print(dir(obj1))
print(' ')
