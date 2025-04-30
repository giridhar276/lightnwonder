
import os
try:
    files = os.listdir()
    for file in files:
        if file.endswith(".csv"):
            os.remove(file)
except Exception as err:
    print(err)
