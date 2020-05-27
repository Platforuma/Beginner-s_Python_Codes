'''
Using Instance Variable
'''
class Employee:
    pass

emp_1 = Employee()
emp_1.first = 'First'
emp_1.last = 'User'
emp_1.pay = 30000
emp_1.email = 'First.User@company.com'

emp_2 = Employee()
emp_2.first = 'Second'
emp_2.last = 'User'
emp_2.pay = 30000
emp_2.email = 'Second.User@company.com'


print(emp_1.email)
print(emp_2.email)
