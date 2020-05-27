'''
Inheritance
adding new attributes
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
        self.pay = int(self.pay * self.amount_raise)

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

class Developer(Employee):
    amount_raise = 1.10
    
class Manager(Employee):
    pass

emp_1 = Employee('First','User', 30000)
emp_2 = Employee('Second','User', 30000)

dev_1 = Developer('Third', 'User', 90000)
dev_2 = Developer('Fourth', 'User', 60000)

mgr_1 = Manager('Fifth', 'User', 90000)
mgr_2 = Manager('Sixth', 'User', 90000)

print('Employee Class Variable: ', Employee.amount_raise)
print('Manager Class Variable: ', Manager.amount_raise)
print('Developer Class Variable: ', Developer.amount_raise)

print(' ')

print('Manager 1 pay before rasie: ', mgr_1.pay)
mgr_1.apply_raise()
print('Manager 1 pay after rasie: ', mgr_1.pay)

print(' ')
print('Developer 1 pay before rasie: ', dev_1.pay)
dev_1.apply_raise()
print('Developer 1 pay after rasie: ', dev_1.pay)

print(' ')
print('Manager 1 amount raised by: ', mgr_1.amount_raise)
print('Developer 1 amount raised by: ', dev_1.amount_raise)
