
import time
from openpyxl import Workbook # excel operations
import openpyxl
print(openpyxl.__version__)
import csv  # reading csv
try:
    string = time.strftime("%d_%B_%Y.xlsx")
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    with open("employeeinfo.csv","r") as fobj:
        reader = csv.reader(fobj)
        for record in reader:
            ws.append(record)
        # Save the file
        wb.save(string)
except Exception as err:
    print(err)