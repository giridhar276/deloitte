
# regular style #
fobj = open("customers.txt","w")
fobj.write("abcd corp")
fobj.close()


# using context manager
# file gets closed automatically
with open("customers.txt","w") as fobj:
    fobj.write("abcd corp")