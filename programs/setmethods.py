

aset = {10,10,10,20,30,30}
bset  = {30,30,30,40,40,50}

aset.add(10)
aset.add(30)
aset.add(40)
print("Updated set: ",aset)
print(bset)

print("Union:",aset.union(bset))
print("Intersection :",aset.intersection(bset))

print("Union :",aset.difference(bset))
print("Intersection :",bset.difference(aset))

print(aset.intersection_update(bset))
print(aset.difference_update())