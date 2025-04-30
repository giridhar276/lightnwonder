


#########################################################################
#Decorating Functions with Parameters
def divide(a, b):
    return a/b
print(divide(2,5))
print(divide(2,0))




#parameters of the nested inner() function inside the decorator is the same as the parameters of functions it decorates. 
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
    
    
divide(2,5)
divide(2,0)
#########################################################################











