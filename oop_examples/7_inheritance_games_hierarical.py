
import random
# Base class
class SlotMachine:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 1000

    def spin(self):
        print(f"{self.player_name} spins the reels...")
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

# Child class 1
class FreeSpinSlot(SlotMachine):
    def free_spin(self):
        print("You've earned a FREE SPIN!")
        self.spin()

# Child class 2
class JackpotSlot(SlotMachine):
    def mega_jackpot(self):
        print("MEGA JACKPOT! You win $5000!")
        self.balance += 5000
        print(f"Updated Balance: ${self.balance}")

# Usage
print("\n--- Hierarchical Inheritance Example ---")
free_spin_player = FreeSpinSlot("Diana")
free_spin_player.spin()
free_spin_player.free_spin()

jackpot_player = JackpotSlot("Ethan")
jackpot_player.spin()
jackpot_player.mega_jackpot()
