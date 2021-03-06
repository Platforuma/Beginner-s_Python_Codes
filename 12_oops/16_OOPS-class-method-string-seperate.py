'''
Class Method
from_String
'''
class Employee:

    amount_raise = 1.04
    num_of_emp = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1
        
    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)

    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)
        #self.pay = int(self.pay * amount_raise)
        self.pay = int(self.pay * Employee.amount_raise)

    @classmethod
    def set_rasie_amt(cls, amount):
        cls.amount_raise = amount
        
emp_1 = Employee('First','User', 50000)
emp_2 = Employee('Second','User', 60000)

str_emp_3 = 'Third-User-25000'
first, last, pay = str_emp_3.split('-')
emp_3 = Employee(first, last, pay)
print(emp_3.email)

str_emp_4 = 'Fourth-User-25000'
first, last, pay = str_emp_4.split('-')
emp_4 = Employee(first, last, pay)
print(emp_4.email)

