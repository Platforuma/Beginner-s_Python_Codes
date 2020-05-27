'''
For the above mentioned program, use getter method to get the
name and balance of the customer and setter method to set the
new name of the customer.
'''
class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def credit(self, deposit):
        self.balance = self.balance + deposit

    def debit(self, withdrawl):
        self.balance = self.balance - withdrawl

cust1 = Account('Saral Jain', 10000)
cust2 = Account('Tim Jones', 5000)

print(cust1.balance)
print(cust1.name)

cust1.credit(50000)
cust1.name = 'Harman'

print(cust1.balance)
print(cust1.name)

cust2.debit(2000)
print(cust2.balance)
print(cust2.name)
