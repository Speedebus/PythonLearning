import random
class dice:
    def roll(self):
        output = (random.randint(1,6),random.randint(1,6))
        return output
dice = dice()
print(dice.roll())

