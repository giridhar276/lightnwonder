
import os
try:
    for val in range(1,10):
        dirname = "dir" + str(val)
        if not os.path.isdir(dirname) and os.path.exists(dirname):
            os.mkdir(dirname)
        else:
            print(dirname,"already created")
except Exception as err:
    print(err)
