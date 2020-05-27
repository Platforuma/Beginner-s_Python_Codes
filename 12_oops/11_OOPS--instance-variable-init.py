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

emp_1 = Employee('First','User', 50000)
emp_2 = Employee('Second','User', 60000)

print(emp_1.email)
print(emp_2.email)
