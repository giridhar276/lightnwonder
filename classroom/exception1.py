import csv
try:
    with open("abc1.csv","r") as fobj:
        reader = csv.reader(fobj)
        for record in reader:
            print(record)
except TypeError as error:
    print(error)
except ValueError as err:
    print(err)
except (KeyError,IndexError) as err:
    print(err)
except FileNotFoundError as err:
    print(err)
except Exception as error:  # Baseclass exception
    print("Unkown error found..",error)
