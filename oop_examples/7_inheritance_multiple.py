
'''
In a game:

Some characters can fly.

Some characters can shoot.

A new character (like a FlyingShooter) can do both — inherit both abilities!
'''

# First parent class
class Flyable:
    def fly(self):
        print("Flying through the air!")

# Second parent class
class Shooter:
    def shoot(self):
        print("Shooting bullets!")

# Child class inheriting from both Flyable and Shooter
class FlyingShooter(Flyable, Shooter):
    def ultimate_attack(self):
        print("Launching ultimate missile!")

# Create instance
hero = FlyingShooter()
hero.fly()           # Inherited from Flyable
hero.shoot()         # Inherited from Shooter
hero.ultimate_attack()  # Own method
