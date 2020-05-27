'''
When ever a customer joins a bank, an account is created
in their name and a balance is set based on how much they deposit.
Then account must also allow for a deposit and credit the acccount.
Upon request the balance of the account and the name of the accounnt holder
will be returned. Also once an account is creaated, the name of the customer
can be changed.
'''
class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def credit(self, deposit):
        self.balance = self.balance + deposit

    def debit(self, withdrawl):
        self.balance = self.balance - withdrawl

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

cust1 = Account('Saral Jain', 10000)
cust2 = Account('Tim Jones', 5000)

print(cust1.get_balance())
print(cust1.get_name())

cust1.credit(50000)
cust1.set_name('Harman')

print(cust1.get_balance())
print(cust1.get_name())

cust2.debit(2000)
print(cust2.get_balance())
print(cust2.get_name())
