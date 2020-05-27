'''
Using Instance Variable
Init method
'''
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print('{} {}'.format(self.first, self.last))
    
emp_1 = Employee('First','User', 50000)
emp_2 = Employee('Second','User', 60000)

##print('{} {}'.format(emp_1.first, emp_2.last))

emp_1.fullname()
emp_2.fullname()
