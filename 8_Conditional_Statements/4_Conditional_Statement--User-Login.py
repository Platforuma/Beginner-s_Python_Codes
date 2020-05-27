'''
Write a Python program which asks for user id and password.
If the data is matched 	with stored data, welcome text is printed.
If the data is not matched, print error.
'''
user1 = 'Platforuma'
pass1 = 'platforuma@123'

user2 = 'adminid'
pass2 = 'adminpass'

user_id = input('Enter user ID: ')

if user_id == user1 or user_id == user2:
    password = input('Enter Password: ')
    if user_id == user1 and password == pass1:
        print('Welcome User 1')
    elif user_id == user2 and password == pass2:
        print('Welcome User 2')
    else:
        print('Invalid Password')
else:
    print('User not found. Kindly sign up')
