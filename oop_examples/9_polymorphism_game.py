"""
Topic: Polymorphism and Method Overriding
This example demonstrates polymorphism and method overriding in Python with clear comments.
"""

# Parent class
class Character:
    def attack(self):
        print("Character attacks with basic punch!")

# Child class: Warrior
class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")

# Child class: Mage
class Mage(Character):
    def attack(self):
        print("Mage attacks with a magic spell!")

# Child class: Archer
class Archer(Character):
    def attack(self):
        print("Archer attacks with a bow and arrow!")

# Create different characters
characters = [Warrior(), Mage(), Archer(), Character()]

# Each character attacks
for char in characters:
    char.attack()
