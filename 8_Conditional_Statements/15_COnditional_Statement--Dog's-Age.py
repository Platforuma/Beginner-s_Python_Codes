'''
Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
'''

human_year = float(input("Enter Dog's Age: "))

if human_year<=2:
    dog_year = human_year * 10.5
    print("Input a dog's age in human years: ", str(human_year))                                    
    print("The dog's age in dog's years is: ", str(dog_year))

else:
    dog_year = ((human_year-2) * 4) + 21
    print("Input a dog's age in human years: ", str(human_year))                                    
    print("The dog's age in dog's years is: ", str(dog_year))
