'''
Inheritance
super __init__function
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
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    

class Manager(Employee):
    amount_raise = 1.10
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('First','User', 30000)
emp_2 = Employee('Second','User', 30000)

dev_1 = Developer('Third', 'User', 90000, 'Python')
dev_2 = Developer('Fourth', 'User', 60000, 'Java')

mgr_1 = Manager('Fifth', 'User', 90000, [dev_1, emp_1])
mgr_2 = Manager('Sixth', 'User', 90000, [])

print("Developer 1 programming language: ", dev_1.prog_lang)
print(" ")

print('Current Manager 1 employee list: ')
mgr_1.print_emp()
print('Current Manager 2 employee list: ')
mgr_2.print_emp()

mgr_1.add_emp(emp_2)
mgr_2.add_emp(emp_1)
mgr_2.add_emp(dev_2)
mgr_1.remove_emp(emp_1)

print('New Manager 1 employee list: ')
mgr_1.print_emp()
print('New Manager 2 employee list: ')
mgr_2.print_emp()
