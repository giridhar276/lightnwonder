# reading line by line
with open("languages1111111.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

# reading using fobj.readlines() --> list   
with open("languages.txt","r") as fobj:
    print(fobj.readlines())

# read using fobj.read()---> string
# ctrl + A   and Ctrl + C
with open("languages.txt","r") as fobj:
    print(fobj.read())


# using csv library
import csv  # builtin library
with open("languages.txt","r") as fobj:
    #convert file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        print(line) # list

# using pandas library - data analytical tool
# pip install pandas  ----> execute in command prompt

import pandas as pd
df = pd.read_csv("languages.txt")
print(df)
