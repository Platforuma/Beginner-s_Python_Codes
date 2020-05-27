'''
Static Method
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
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.amount_raise)

    @classmethod
    def set_rasie_amt(cls, amount):
        cls.amount_raise = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        
emp_1 = Employee('First','User', 50000)
emp_2 = Employee('Second','User', 60000)

str_emp_3 = 'Third-User-25000'
emp_3 = Employee.from_string(str_emp_3)
print(emp_3.email)

emp_4 = Employee.from_string('Fourth-User-45000')
print(emp_4.email)

import datetime
my_date = datetime.date(2019,3,2)
print(Employee.is_working(my_date))
