#In your game, every character (enemy, player, boss) can move and attack.

#But Player has special things (special powers) that base character doesn't have.

# Parent class
class Character:
    def move(self):
        print("Character is moving.")

    def attack(self):
        print("Character is attacking.")

# Child class inheriting from Character
class Player(Character):
    def special_ability(self):
        print("Player uses a special ability!")

# Create Player instance
p = Player()
p.move()            # Inherited from Character
p.attack()          # Inherited from Character
p.special_ability() # Own method