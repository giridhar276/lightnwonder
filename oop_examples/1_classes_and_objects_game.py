

import os
import shutil

# Define a class
class GameAssetManager:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path  # Instance variable: where the asset is currently
        self.destination_path = destination_path  # Instance variable: where we want it in the game folder

    def display_paths(self):
        """Display source and destination paths"""
        print(f"Asset Source Path: {self.source_path}")
        print(f"Asset Destination Path: {self.destination_path}")

    def copy_asset(self):
        """Copy game asset from source to destination"""
        try:
            shutil.copy(self.source_path, self.destination_path)
            print(f"Asset copied successfully from {self.source_path} to {self.destination_path}")
        except FileNotFoundError:
            print(f"Error: Source asset not found - {self.source_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Create GameAssetManager objects (instances)
    player_sprite = GameAssetManager("assets/original/player.png", "game_assets/player_copy.png")
    #background_music = GameAssetManager("assets/original/bg_music.mp3", "game_assets/bg_music_copy.mp3")

    # Access methods
    player_sprite.display_paths()
    player_sprite.copy_asset()

    print()

    #background_music.display_paths()
    #background_music.copy_asset()
