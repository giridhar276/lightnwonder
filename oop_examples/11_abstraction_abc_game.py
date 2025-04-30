

"""
Slot Machine Game Example using Abstraction
Demonstrates real-world use of abstraction using abstract base classes (ABC).
No symbols used — just strings and numbers.
"""

from abc import ABC, abstractmethod
import random

# -------------------------------------------------------------------
# Abstract Base Class for Slot Machines
# -------------------------------------------------------------------

class SlotMachine(ABC):
    """
    Abstract class for all slot machines.
    Enforces 'spin' and 'payout' to be implemented in all child classes.
    """
    @abstractmethod
    def spin(self):
        pass

    @abstractmethod
    def payout(self):
        pass

# -------------------------------------------------------------------
# 🎰 Classic Slot Machine
# -------------------------------------------------------------------

class ClassicSlotMachine(SlotMachine):
    def __init__(self):
        self.reels = ["Cherry", "Lemon", "Bell"]
        self.last_spin = []

    def spin(self):
        # Randomly pick 3 items from the reels
        self.last_spin = [random.choice(self.reels) for _ in range(3)]
        print("Classic Slot Result:", self.last_spin)

    def payout(self):
        # Win if all 3 symbols are the same
        if len(set(self.last_spin)) == 1:
            print(">>> JACKPOT! You win 100 coins!")
        else:
            print(">>> Try again.")

# -------------------------------------------------------------------
#  Video Slot Machine
# -------------------------------------------------------------------

class VideoSlotMachine(SlotMachine):
    def __init__(self):
        self.reels = ["Gold", "Silver", "Diamond", "Ruby"]
        self.last_spin = []

    def spin(self):
        # Randomly pick 5 items from the reels
        self.last_spin = [random.choice(self.reels) for _ in range(5)]
        print("Video Slot Result:", self.last_spin)

    def payout(self):
        # Win if at least 3 items match
        max_match = max(self.last_spin.count(item) for item in set(self.last_spin))
        if max_match >= 3:
            print(f">>> Match of {max_match}! You win {max_match * 50} coins!")
        else:
            print(">>> No significant match.")

# -------------------------------------------------------------------
#  Game Engine
# -------------------------------------------------------------------

def play_game(machine: SlotMachine):
    """
    Plays the given slot machine (works with any subclass).
    """
    machine.spin()
    machine.payout()
    print("-" * 40)

# -------------------------------------------------------------------
#  Run the Game
# -------------------------------------------------------------------

if __name__ == "__main__":
    classic_machine = ClassicSlotMachine()
    video_machine = VideoSlotMachine()

    print("Playing Classic Slot Machine")
    play_game(classic_machine)

    print("Playing Video Slot Machine")
    play_game(video_machine)
