'''
Die Game
'''
import random

class DieGame:

    def __init__(self):
        self.side = 0

    def throw(self):
        self.side = random.randint(1,7)

    def get_value(self):
        return self.side

for i in range(1,10):
    my_die = DieGame()
    my_die.throw()
    print('The value of die is' , my_die.get_value())
