'''
Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
sample_list = ['p', 'q']
num = input('Enter the number: ')

new_list1 = []
for i in sample_list:
    for x in range(1,int(num)+1):
        new_list1.append(i+str(x))

print(new_list1)


new_list2 = []
for x in range(1,int(num)+1):
    for i in sample_list:
        new_list2.append(i+str(x))

print(new_list2)
