#method1
ip = "192.168.{}.{}"
for val in range(0,2):
    for ival in range(1,11):
        finalip= ip.format(val,ival)
        print(finalip)


#method2
ip = "192.168."
for val in range(0,2):
    newip = ip + str(val)
    for ival in range(1,11):
        finalip = newip + "." + str(ival)
        print(finalip)