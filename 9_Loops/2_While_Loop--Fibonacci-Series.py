'''
Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''

#using only while loop
print('----Simplest Code----')

x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y

print(' ')

#using while loop and list:
print('----While Loop and List----')
fib_list = ['0', '1']

while True:
    item = int(fib_list[-1]) + int(fib_list[-2])
    if item<51:
        fib_list.append(str(item))
    else:
        break
    
print('Fibonacci List: ', fib_list)
print('Fibonacci Series: ', ', '.join(fib_list))








