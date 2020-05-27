'''
Write a program that computes the net amount of a bank account based a transaction
log from console input. The transaction log format is shown as following:
	D 100
	W 200
	D means deposit while W means withdrawal.
	Suppose the following input is supplied to the program:
	D 300
	D 300
	W 200
	D 100
	Then, the output should be:
	500
'''

net_amount = 0

while True:
    operation = input("Enter the operation (D/W): ")

    if operation=='D' or operation=='d':
        value = float(input("Enter the amount: "))
        net_amount += value

    elif operation=='W' or operation=='w':
        value = float(input("Enter the amount: "))
        net_amount -= value

    else:
        break

print("Total Amount: ", str(net_amount)) 
                  
