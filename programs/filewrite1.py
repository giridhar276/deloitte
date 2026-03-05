# regular way
#case1: if the file is not found.. file gets created
#case2: if the file found.... it overwrites the existing code
fobj = open("languages.txt","w")
fobj.write("python\n")
fobj.writelines(["unix","java","oracle\n"])

for val in range(1,10):
    fobj.write(str(val) + "\n")
fobj.close()

# pythonic way
# context manager 
# if any line begins using 'with' keyword .. it is called as context manger
# when the file is out of indentation .. file gets closed automatically.
# Advantage: file gets closed automatically.


with open("languages.txt","w") as fobj:
    fobj.write("python\n")
    fobj.writelines(["unix","java","oracle\n"])

