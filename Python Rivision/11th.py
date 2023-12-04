# inbuilt module -> random
from random import randint

class Dice:
    '''Dice'''
    def roll(self):
        '''roll'''
        first = randint(1, 6)
        second = randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())
