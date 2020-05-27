'''
Class Variables
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
        
        
emp_1 = Employee('First','User', 50000)
emp_2 = Employee('Second','User', 60000)

print('Number of Employee: ', Employee.num_of_emp)
print(' ')

emp_3 = Employee('Third','User', 50000)
emp_4 = Employee('Fourth','User', 60000)

print('Number of Employee: ', Employee.num_of_emp)
print(' ')

