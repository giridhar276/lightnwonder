alist = [10,5,43,56,34,5,43]
alist.append(100)
print("After appending:",alist)
alist.extend([51,93,34])
print("AFter extending:",alist)
alist.insert(1,120)
print("After insering:",alist)
# value at that index will be removed
alist.pop(1) # 1 is the index
print("After pop:",alist)
# will remove the value directly
if 193 in alist:
    alist.remove(193)
else:
    print("value is not found")

alist.reverse()  # reversing list elements
print("Reversing:",alist)
alist.sort()  # ascending order
print("After sorting :",alist)
alist.sort(reverse=True)# descending order
print("After sorting:",alist)


alist = [10,5,43,56,34,5,43]
for val in alist:
    print(val)

name = "python"
for char in name:
    print(char)

for val in range(1,10):
    print(val)

for val in range(1,10,2):
    print(val)


alist= [10,5,5,5,43,56,5,34,5,43]
alist.remove(5) # will remove the 1st occu
print(alist)

# write a program to remove all the 
# occurences of 5

for val in range(0,alist.count(5)):
    alist.remove(5)
print(alist)