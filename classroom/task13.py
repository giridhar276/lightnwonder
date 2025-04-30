
import time
import datetime
import os
import calendar
# current working directory
print(os.getcwd())
# display login
print(os.getlogin())
# all environment variables
#print(os.environ)
for key,value in os.environ.items():
    print(key)
    print(value)
    print("--------")
## display todays timestamp
print(datetime.datetime.now())
print(calendar.month(2025,4))
print(calendar.calendar(2025))

#### display all the files and its size
for file in os.listdir():
    print(file.ljust(15), os.path.getsize(file),"bytes")

# get modified time of the time
for file in os.listdir():
    modifedepoch = os.path.getmtime(file) # get epoch
    # converting epoch value to understandable format
    timestamp = datetime.datetime.fromtimestamp(modifedepoch)
    print(file.ljust(20),timestamp)