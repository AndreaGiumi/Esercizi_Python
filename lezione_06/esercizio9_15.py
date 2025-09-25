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


    def simulate_until_win(self, my_ticket):
        attempts = 0
        while True:
            simulate_ticket = random.choices(self.lotteryList, k=4)
            if simulate_ticket == my_ticket:
                print("You win")
                break
            attempts += 1
            print(my_ticket)
            print(simulate_ticket)
            print(attempts)

      
ciao = LotteryMachine()

my_ticket = [34, 53, "R", 9]
ciao.simulate_until_win(my_ticket)
