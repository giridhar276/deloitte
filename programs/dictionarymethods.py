book = {"chap1":10 ,"chap2":20 ,"chap3":30}
print("Initial dictionary:",book)
# add key-value
book["chap4"] = 40
book["chap5"] = 50
print(book)
print(book["chap1"]) # 10
print(book["chap2"]) # 20 

# methods
print(book.keys())

for key in book.keys():
    print(key)

for key in book:
    print(key)

# values
print(book.values())

for v in book.values():
    print(v)

# items 
for k,v in book.items():
    print(k,v)

#dict.pop(key)
book.pop("chap1")   #book.pop(key) # key-value will be removed from dictionary
print("After pop operation :",book)


book.popitem()   # last inserted key and value will be removed
print(book)
book.popitem()   # last inserted key and value will be removed
print(book)

# combine 2 dictionaries
book = {"chap1":10,"chap2":20}
newbook = {"chap3":30}
#method1
finalbook = {**book,**newbook}
print(finalbook)
# method2 - book is getting updated
book.update(newbook)
print(book)
book["chap1"] =[10,20,30,40,50]
print(book)