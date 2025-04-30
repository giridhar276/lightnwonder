# fixed arguments
def display(a,b):
    c = a + b
    return c
total = display(10,20)
print(total)

# default arguments
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display()
display(10)
display(10,20)
display(10,20,30)

# keyword arguments
def display(c,a,b):
    print(a,b,c)
display(b=20,a=10,c=30)

# variable length arguments
def display(*args):
    print(type(args))
    for val in args:
        print(val)
display(10,20,30,40,6,54,65,43,6,43,4,4)

def displayinfo(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
displayinfo(chap1=10 ,chap2 = 20)