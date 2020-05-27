'''
Write a program that calculates and prints the value according to the given formula:
	Q = Square root of [(2 * C * D)/H]
	Following are the fixed values of C and H:
	C is 50. H is 30.
	D is the variable whose values should be input to your program in a comma-separated sequence.
Example: Let us assume the following comma separated input sequence is given to the program:
	100,150,180
	The output of the program should be:
	18,22,24
'''
d = input('Enter the values of D: ')
d = d.split(',')

C = 50
H = 30

result = []

for i in d:
    Q = ((2*C*int(i))/H)**(1/2)
    Q = int(Q)
    result.append(str(Q))

print(','.join(result))
