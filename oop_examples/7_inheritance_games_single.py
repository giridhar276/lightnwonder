import random

# Base class for a slot game
class SlotMachine:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 1000  # Starting money

    def spin(self):
        print(f"{self.player_name} is spinning the reels... 🎰")
        symbols = ["Cherry", "Lemon", "Bell", "Seven", "Diamond"]
        result = [random.choice(symbols) for _ in range(3)]
        print(f"Spin Result: {result}")
        self.check_win(result)

    def check_win(self, result):
        if result.count(result[0]) == 3:
            print(f"JACKPOT!!! 🎉 All {result[0]}s! You win $500!")
            self.balance += 500
        elif result.count(result[0]) == 2 or result.count(result[1]) == 2:
            print("Small Win! You win $100!")
            self.balance += 100
        else:
            print("No win. You lose $50.")
            self.balance -= 50

        print(f"Current Balance: ${self.balance}")

# Derived class with Bonus Game feature
class BonusSlotMachine(SlotMachine):
    def __init__(self, player_name):
        super().__init__(player_name)

    def bonus_round(self):
        print(f"{self.player_name} triggered BONUS ROUND! 🎉🎉")
        bonus_win = random.randint(100, 1000)
        print(f"You win an additional bonus of ${bonus_win}!")
        self.balance += bonus_win
        print(f"New Balance after bonus: ${self.balance}")

# Example gameplay
if __name__ == "__main__":
    # Create player
    player = BonusSlotMachine("Alice")

    # Gameplay sequence
    player.spin()
    player.spin()
    player.bonus_round()
    player.spin()
