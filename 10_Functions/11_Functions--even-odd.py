'''
Define a function that can accept an integer number as input
and print the "It is an even number" if the number is even,
otherwise print "It is an odd number".
'''


def checkValue(num):
    if num%2==0:
        print(str(num), 'is an even number')
    else:
        print(str(num), 'is an odd number')

checkValue(8)
checkValue(101)
checkValue(3)
checkValue(256)
checkValue(87)
checkValue(1)
