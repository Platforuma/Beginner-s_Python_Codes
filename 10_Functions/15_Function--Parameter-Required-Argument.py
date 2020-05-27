#--------Required Argument Function-----------
def helloName(name):
   return 'Hello ' + name

print(helloName('Saral'))
print(' ')

#---------Keyword Argument Function------------------
def myInfo(name, age):
   return 'Name: ' + name + '\n' + 'Age: ' + str(age)

print(myInfo(age=18, name="Saral"))
print(myInfo(name="Pradeep", age=24))
print(' ')

#---------Default Argument Function------------------
def basicInfo(name, age = 23, language = 'python'):
   return 'Name: ' + name + '\n' + 'Age: ' + str(age) + '\n' + 'Language: ' + language 

print(basicInfo(age=18, name="Saral"))
print(basicInfo(name="Pradeep", language='embedded c' ))
print(' ')
