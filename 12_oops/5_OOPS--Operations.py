'''
Method Parameters and self
'''
class Operations:
    '''Double the value'''
    def double_value(self, value):
        double = value * 2
        return double

    def add_value(self, a, b):
        add = a + b
        return add

obj1 = Operations()
print(obj1.double_value(2))
print(obj1.add_value(2,3))
