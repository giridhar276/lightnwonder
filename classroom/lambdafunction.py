# traditional way
def display(a,b):
    c = a + b
    return c
total = display(10,20)
print(total)

# lambda function  # pythonic way
# lambda is the single liner function
#syntax:
#functioname = lambda variables: expression
display = lambda a,b : a + b
total = display(10,20)
print(total)

display = lambda *args : sum(args)
total = display(10,20,56,4,56,43,4,4,456,43,45,433,42)
print(total)



alist = [10,20,30,40]
#[15,25,35,45]
blist = []
for val in alist:
    blist.append(val + 5)
print(blist)


#map(function,iterable)
def increment(x):
    return x+ 5
print("Using map:")
print(list(map(increment,alist)))

####### using map with lambda
increment = lambda x : x+5
print(list(map(increment,alist)))

####### using map with lambda - in same line
print(list(map(lambda x : x+5,alist)))



