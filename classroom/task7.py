import csv
workset = set()
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        workset.add(workclass)
    # displaying
    for work in workset:
        print(work)
    
import csv
workdict  = dict()
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        workdict[workclass] = 1  # {"public":1,"private":1}

    # displaying
    for work in workdict:
        print(work)