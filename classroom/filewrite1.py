# If the file doesnt exist.. file will be created first
# If the file is already existing with content, it overwrites

#fobj = open("C:\\new\\languages.txt","w")
#fobj = open(r"C:\languages.txt","w") # rawstring
#fobj = open("C:/new/new/languages.txt","w")
# traditional way  # regular
fobj = open("languages.txt","w")
fobj.write("python\n")
fobj.write("unix\n")
fobj.writelines(["java","spark"])
for num in range(1,10):
    fobj.write(str(num) + "\n")
fobj.close()


# pythonic way
# context manager
# if any line starts with keyword 'with'.. we call it as context manager
# Advantage: file gets closed automatically
# database connections , network connections , socket connections
with open("languages.txt","w") as fobj:
    fobj.write("python\n")
    fobj.write("unix\n")
    fobj.writelines(["java","spark"])

