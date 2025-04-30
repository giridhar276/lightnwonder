import random

# Base class1
class SlotMachine:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 1000

    def spin(self):
        print(f"{self.player_name} spins the machine...")
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

# Another base class
class LoyaltyProgram:
    def __init__(self):
        self.points = 0

    def add_points(self, amount):
        self.points += amount
        print(f"Loyalty Points Earned: {amount}, Total: {self.points}")

# Derived class using multiple inheritance
class VIPSlotMachine(SlotMachine, LoyaltyProgram):
    def __init__(self, player_name):
        SlotMachine.__init__(self, player_name)
        LoyaltyProgram.__init__(self)

    def spin(self):
        print("VIP Spin Activated! 💎")
        super().spin()
        self.add_points(20)

# Usage
print("\n--- Multiple Inheritance Example ---")
vip_player = VIPSlotMachine("Bob")
vip_player.spin()
vip_player.spin()
