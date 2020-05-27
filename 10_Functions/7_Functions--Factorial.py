'''
Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.
'''

def factorial(num):
    result = 1
    if num==0:
        return 1
    elif num<0:
        return 'Wrong Input'
    else:
        for i in range(1,num+1):
            result = result * i
        return 'Factorial of', num, 'is', result

print(factorial(4))
print(factorial(-14))
print(factorial(5))
print(factorial(0))
print(factorial(3))
print(factorial(4))

