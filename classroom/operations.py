
import os
import platform
def displayos():
    print(os.name)

def displaycwd():
    print(os.getcwd())

def displayuser():
    print(os.getlogin())

def getplatform():
    print(platform.platform())

# if the program is executed directly below condition becomes True
#if this program is imported to other program, below condition becomes False
if __name__ == "__main__":
    displayos()
    displaycwd()
    displayuser()
    getplatform()