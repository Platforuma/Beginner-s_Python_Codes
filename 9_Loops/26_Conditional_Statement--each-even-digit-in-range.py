'''
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number
'''

values = []

for num in range(1000,3001):
    num = str(num)
    if int(num[0])%2==0 and int(num[1])%2==0 and int(num[2])%2==0 and int(num[3])%2==0:
        values.append(num)

print (",".join(values))



