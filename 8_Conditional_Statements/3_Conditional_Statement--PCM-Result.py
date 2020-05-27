'''
Write a Python program which accepts Physics, Chemistry & Math marks.
Sum it up and get the % scored. Based on it divided the student as:

marks < 40: ‘betaji, tumse na ho pai’

40<makrs<80: ‘Sharma ji k ladke ko dekha hai’

marks>80: ‘beta, thoda aur’
'''

physics = int(input('Enter Physics marks: '))
chemistry = int(input('Enter Chemistry marks: '))
maths = int(input('Enter Maths marks: '))

total = physics + chemistry + maths
print('Total marks: ', str(total))

per = ((total)/300) * 100
print('Total %: ', str(per))

if per<=40:
    print('betaji, tumse na ho pai')
elif per>40 and per<=80:
    print('Sharma ji k ladke ko dekha hai')
else:
    print('beta, thoda aur')
