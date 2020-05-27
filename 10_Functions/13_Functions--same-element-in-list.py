'''
Write a Python function that takes two lists and returns True if they
have at least one common member
'''

def identifier(list1, list2):
    result = False
    for i in list1:
        for j in list2:
            if i==j:
                result = True
                return result
            

print(identifier([1,2,3,4,5],[6,7,8,9]))
