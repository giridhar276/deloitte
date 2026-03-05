alist = [10,20,56,34,67,37,82]
alist.append(92)  # adding single object
print("After appending :",alist)
alist.extend([74,71,17]) # adding set of values
print("After extending:",alist)
alist.insert(1,100)  # list.insert(index,value)
print("AFter inserting :",alist)
alist.pop(1)   # list.pop(index)
print("After pop operation :",alist)
if 20 in alist:
    alist.remove(20)
    print("After removing :",alist)
else:
    print("value not in list")

# sorting in ascending order
alist.sort()
print("sorting in ascending order :",alist)
alist.sort(reverse=True)
print("sorting in descending order :",alist)
alist.reverse()
print("reversing values :",alist)