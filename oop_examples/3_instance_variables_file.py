"""
Topic: Instance Variables and Methods
Demonstrating how each object has its own copy of instance variables.
"""

# File handling example using similar class structure

class FileHandler:
    def __init__(self, filename):
        self.filename = filename  # instance variable

    def write_content(self, content):
        """Write content to the file"""
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            print(f"Content written to {self.filename}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def read_content(self):
        """Read and display content from the file"""
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
            print(f"Content of {self.filename}:")
            print(data)
        except FileNotFoundError:
            print(f"Error: File {self.filename} not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

# Example usage
file1 = FileHandler("sample1.txt")
file2 = FileHandler("sample2.txt")

file1.write_content("Hello! This is file 1.")
file2.write_content("Hi there! This is file 2.")

file1.read_content()
file2.read_content()
