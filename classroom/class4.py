import os
import csv
class FileOperation:
    def __init__(self,filename):
        self.filename = filename
    def readFile(self):
        try:
            if os.path.isfile(self.filename):
                with open(self.filename,"r") as self.fobj:
                    self.reader = csv.reader(self.fobj)
                    for line in self.reader:
                        print(line)
        except Exception as err:
            print(err)
        except Exception as err:
            print(err)
if __name__ == "__main__":
    file = FileOperation("employeeinfo.csv")
    file.readFile()