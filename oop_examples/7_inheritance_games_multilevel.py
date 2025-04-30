
import random
# Base class
class SlotMachine:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 1000

    def spin(self):
        print(f"{self.player_name} is spinning the slot...")
        symbols = ["Cherry", "Lemon", "Bell", "Seven", "Diamond"]
        result = [random.choice(symbols) for _ in range(3)]
        print(f"Result: {result}")
        self.check_win(result)

    def check_win(self, result):
        if result.count(result[0]) == 3:
            print("JACKPOT! You win $500")
            self.balance += 500
        elif result.count(result[0]) == 2 or result.count(result[1]) == 2:
            print("Small Win! You win $100")
            self.balance += 100
        else:
            print("You lost $50")
            self.balance -= 50
        print(f"Balance: ${self.balance}")

# First-level derived class
class BonusSlotMachine(SlotMachine):
    def bonus_round(self):
        print("Bonus Round Unlocked!")
        bonus = random.randint(100, 1000)
        print(f"You win ${bonus} in bonus!")
        self.balance += bonus
        print(f"New Balance: ${self.balance}")

# Second-level derived class
class SuperBonusSlotMachine(BonusSlotMachine):
    def lucky_draw(self):
        print("Lucky Draw Activated!")
        prize = random.choice(["Car", "iPhone", "Vacation", "$1000"])
        print(f"You won a {prize}!")

# Usage
print("\n--- Multilevel Inheritance Example ---")
super_player = SuperBonusSlotMachine("Carol")
super_player.spin()
super_player.bonus_round()
super_player.lucky_draw()
