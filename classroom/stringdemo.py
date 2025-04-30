name = "python programming"
print(name)
# string[start:stop:step]
print("I love",name)
print(name[0])
print(name[1])
print(name[0:8])
print(name[8:11])
print(name[0:18])
print(name[0:18:2])  # p t  o   r g a
print(name[8:14:3])
print(name[:])  #  print(name)  #print(name[0:])
print(name[::])
print(name[-1])
print(name[-5:-2]) # m
print(name[::-1])


print(name.capitalize())
print(name.title())
print(name.count("p"))
print(name.split(" "))
print(name.split("p"))
print(name.endswith("g"))
print(name.endswith("m"))
print(name.startswith("p"))
print(name.split(" "))
print(name.replace("python","ruby"))
print(name.center(40)) 
print(name.center(40,"*")) 
print(name.find("in")) # it returns index if substring found
                      # if not found ... it returns -1

print(name.isupper())
print(name.islower())
print(name.isalpha())

aname = " python  "
print(len(aname.strip())) # remove whitespaces at both ends
print(len(aname.rstrip()))
print(len(aname.lstrip()))

aname = "I love {} and {}" # template
print(aname.format("python","datascience"))
# simple if
if name.isupper():
    print("string is upper")
    print("inside if")
    print("still inside if")

# if-else
if name.isupper():
    print("string is upper")
    print("inside if")
    print("still inside if")
else:
    print("string is lower")
    print("inside else")



