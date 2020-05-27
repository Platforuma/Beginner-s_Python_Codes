'''
Write a python program to get all the prime numbers between 1 to 100
'''
#for method
print('----List and For Loop----')

primes = []
for possiblePrime in range(2, 51):
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        primes.append(possiblePrime)

print(primes)

print(' ')

#NESTED LOOP
print('----Nested Loop----')

i = 2
while(i<50):
    j = 2
    while(j<=(i/j)):
        if not (i%j):
            break
        j = j + 1
    if (j>(i/j)):
        print(str(i), ' is prime')
    i = i + 1


print(' ')


