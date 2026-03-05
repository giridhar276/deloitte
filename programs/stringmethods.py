
# p    y    t     h     o     n        p      r     o    g     r    a     m    m     i      n    g
# 0    1    2     3     4     5   6    7      8     9   10    11    12   13   14    15     16   17
name = "python programming"
# slicing 
# string[start:stop:step]
print(name[0:8])
print(name[8:14])
print(name[0:18:2])   # pto rga
print(name[1:18:4])   # ynom
print(name[-1])
print(name[::])
print(name[::-1])
# methods
print(name.capitalize())
print(name.count("p"))
print(name.upper())
print(name.isupper())
print(name.lower())
print(name.islower())
print(name.endswith("g"))   #True
print(name.startswith("m")) #False
print(name.split(" "))
print(name.replace("python","java"))
# string template
aname = "I love {} and {}"
print(aname.format("Hyderabad","bangalore"))
print(aname.format("java","python"))
aname = " python  "
print(aname.strip()) # will remove whitespaces at both ends
print(aname.lstrip())# remove whitepsaces only at left side 
print(aname.rstrip())