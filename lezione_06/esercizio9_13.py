import random

class Dice:
    def __init__(self, side=6):
        self.side = side

    def roll_dice(self):
        roll = random.randint(1, self.side)
        print(roll)

dice_6 = Dice()

dice_6.roll_dice()


dice_10 = Dice(10)

dice_10.roll_dice()


dice_20 = Dice(20)
dice_20.roll_dice()