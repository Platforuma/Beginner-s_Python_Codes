'''
__INIT__ method
'''

class CurrentAccount:

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def get_customer_name(self):
        return self.customer_name

obj1 = CurrentAccount('Saral Jain')
print(obj1.get_customer_name())

obj2 = CurrentAccount('Pradeep Kurmi')
print(obj2.get_customer_name())
