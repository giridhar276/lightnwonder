
#In all examples, we didn't care about the class name.
#We only cared that the object had the correct method.


class Bird:
    def move(self):
        print("Bird is flying in the sky! 🐦")

class Fish:
    def move(self):
        print("Fish is swimming in the water! 🐟")

class Human:
    def move(self):
        print("Human is walking on land! 🚶")

# Game engine move function
def move_character(character):
    character.move()

# Create characters
bird = Bird()
fish = Fish()
human = Human()

# Move all characters
move_character(bird)
move_character(fish)
move_character(human)




