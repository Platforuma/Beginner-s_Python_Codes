'''
Class Method
amount_rasie
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

print('Before function execution: ', Employee.amount_raise)

Employee.set_rasie_amt(1.06)

print('After function execution: ', Employee.amount_raise)
print(' ')
print('Employee 1 amount rasie: ', emp_1.amount_raise)
print('Employee 2 amount rasie: ',emp_2.amount_raise)

print('Pay before rasie: ', emp_1.pay)
emp_1.apply_raise()
print('Pay after rasie: ', emp_1.pay)

print(' ')
print('Number of Employee: ', Employee.num_of_emp)
print(' ')

print('Class amount rasie: ', Employee.amount_raise)
print('Emp_1 amount rasie: ', emp_1.amount_raise)
print('Emp_2 amount rasie: ', emp_2.amount_raise)
print(' ')

#change class variable for only one instance
emp_1.amount_raise = 1.08

print('Class amount rasie: ', Employee.amount_raise)
print('Emp_1 amount rasie: ', emp_1.amount_raise)
print('Emp_2 amount rasie: ', emp_2.amount_raise)
print(' ')

#change class variable for whole class
Employee.amount_raise = 1.06

print('Class amount rasie: ', Employee.amount_raise)
print('Emp_1 amount rasie: ', emp_1.amount_raise)
print('Emp_2 amount rasie: ', emp_2.amount_raise)



