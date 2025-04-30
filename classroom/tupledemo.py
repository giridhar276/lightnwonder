# typecasting 
atup = (10,20,45,43)
alist = list(atup) # conveerting to list
alist.append(400)  # making changes
alist[0] = 100
atup = tuple(alist) # reconverting back
print("tuple values:",atup)