



ip = "192.168.0.{}"  #template
for val in range(1,101):
    print(ip.format(val))


ip = "192.168.0."
for val in range(1,101):
    finalip = ip + str(val)
    print(finalip)