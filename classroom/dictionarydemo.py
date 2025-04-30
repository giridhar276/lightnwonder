book = {"chap1":10,"chap2":20,"chap3":30}
print(book)
# add new key:value pairs
book['chap4'] = 40
book["chap5"] = 50
print(book)
# access individual value
print(book["chap1"])
print(book["chap2"])
print(book.get("chap1"))
print(book.get("chap9"))  # None
#print(book["chap10"])

if "chap10" in book:
    print(book["chap10"])
else:
    print("key not found")

# display keys
print(book.keys())
# display values
print(book.values())
# display pairs
print(book.items())
# delete key-value
book.pop("chap1") # chap1-10 will be removed
print(book)
book.popitem()  # will remove last key-value
print(book)
# combining dictionaries
newbook = {"chap6":60,"chap7":70} #method1
finalbook = {**book,**newbook}
print(finalbook)
#method2
book.update(newbook)
print(book)


# iterating keys
for key in book.keys():
    print(key)
# iterating values
for value in book.values():
    print(value)
# iteraing items
for k,v in book.items():
    print("Key :", k)
    print("Value:",v)





