import random
import string

class LotteryMachine:
    def __init__(self):
        
        self.nums = [random.randint(0,99) for _ in range(10)]
        self.letts = [random.choice(string.ascii_uppercase) for _ in range(5)]
        self.lotteryList = self.nums + self.letts


    def win_ticket(self):
        self.ranT = random.choices(self.lotteryList, k=4)
        print(self.ranT)

    def you_win(self):
        print(f"Se il tuo ticket è {self.ranT}, hai vinto il premio")


ciao = LotteryMachine()
ciao.win_ticket()

ciao.you_win()