
import csv
mcount = 0
fcount = 0
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    for record in reader:
        gender = record[9].lstrip()
        if gender == "Male":
            mcount = mcount +1
        elif gender == "Female":
            fcount = fcount + 1
    print("Total male count:", mcount)
    print("Total female count:",fcount)

import csv
genderlist = list()
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    for record in reader:
        gender = record[9].lstrip()
        genderlist.append(gender)

    print("Total male count:", genderlist.count("Male"))
    print("Total female count:",genderlist.count("Female"))
