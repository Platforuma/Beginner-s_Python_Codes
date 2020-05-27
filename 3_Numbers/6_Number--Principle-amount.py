'''
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12450
'''

principle_amount = float(input("Enter the Principle Amount: "))
time = float(input("Enter the number of years: "))
rate = float(input("Enter the rate: "))

total_amount = principle_amount + principle_amount*time*rate/100
print("Your total amount will be: ", str(total_amount))
