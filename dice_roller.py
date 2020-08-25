import re
import random
from random import randint

class DiceRoller:
    def __init__(self):
        # by default uses system time
        random.seed

    def roll(self, max_val=1):
        return randint(1, max_val)

    def roll_multiple(self, dice_count=1, die_max_val=1):
        total = 0
        for die in range(dice_count):
            total += self.roll(die_max_val)
        return total

    def roll_die_string(self, die_string=''):
        # print("die string: {die_string}").format(die_string=die_string)
        dice_count, die_max_val = map(int, die_string.split('d'))
        return str(self.roll_multiple(dice_count, die_max_val))

    # parse die rolls and modifiers into a value
    # e.g 1d4 + 1d6 - 1d8 + 10 - 20
    def roll_string(self, roll_text=''):
        # the lambda is used to call roll_die_string to replace the die notation
        # match.group() gets the actual string that the match found
        # BUG: Regex needs to be updated for things like 10d10 where there are more than 3 characters
        replaced_rolls = re.sub(r'\d*d\d*', lambda match: self.roll_die_string(match.group()), roll_text)
        # print("replaced roll: {replaced_rolls}").format(replaced_rolls=replaced_rolls)
        return eval(replaced_rolls)
