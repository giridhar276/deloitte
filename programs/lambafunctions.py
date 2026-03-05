# regular way
def display(a,b):
    c = a + b
    return c
total = display(10,20)


# pythonic way
# lambda function 
# lambda is the replacement of single liner function 
# syntax: functioname = lambda variables : expression

display = lambda a,b : a + b
total = display(10,20)


# length of the string 
length = lambda x : len(x)
print(length("python"))

# convert to tupper
myupper = lambda s : s.upper()
print(myupper("hello"))

#max of 2 numbers
maximum = lambda a,b: a if a> b else b
print(maximum(10,20))

# positive , negative or zero 
status = lambda x : "positive" if x > 0 else  "Negative" if x < 0 else "zero"
print(status(5))

# grade categorization
grade = lambda x : "A" if x>=90 else  "B" if x>=75 else "C"
print(grade(80))

# password check
password_check = lambda pwd : "string" if len(pwd) >=8 else "weak"
print(password_check("pass123"))



alist = ["python","unix","C"]
blist = []
for value in alist:
    blist.append(len(value))
print(blist)

#map(functio,iterable)
alist = ["python","unix","C"]
print(list(map(lambda x: len(x),alist)))

## just for your understnaind
data = [1,2,3]
print(max(data))

### example
models = [
    {"name":"model1","accuracy":0.85},
    {"name":"model2","accuracy":0.65},
    {"name":"model3","accuracy":0.90}
]


print(models[0]["accuracy"])  

getbest = max(models , key = lambda m :m['accuracy'])
print(getbest.get("accuracy"))
print(getbest["accuracy"])



for val in range(1,10):
    print(val)
#list comprehesion
#obj = [ expression forloop ]
output = [val   for val in range(1,11)]
print(output)

#############################
# biggest file in current folder
##############################
import os 
files = [file  for file in os.listdir(".") if os.path.isfile(file)]
biggest = max(files, key = lambda f: os.path.getsize(f))
print(biggest,os.path.getsize(biggest),"bytes")

##################################
## without lambda and list comprehension
####################################
def getsize(filename):
    return os.path.getsize(filename)

files = []
for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)

biggest = max(files , key = getsize)
print(biggest, os.path.getsize(biggest))


## sorting dates 
from datetime import datetime
dates = ["2026-02-01","2025-12-10","2026-01-05"]
sorteddates = sorted(dates , key = lambda d : datetime.strptime(d,"%Y-%m-%d"))
print(sorteddates)

alist = [10,20,30]
def increment(x):
    return x + 5
print(list(map(increment,alist)))

# increment 5 to all the values
alist = [10,20,30]
#[15,25,35]
#map(function,iterable)
print(list(map(lambda x:x +5,alist)))


largest = max(alist)
print(list(filter(lambda x:x == largest,alist)))

numbers = [1,45,4,64,443]
evens = list(filter(lambda x: x %2 ==0, numbers))
print(evens)

strings = ["ram","python","C","cobol"]
data = list(filter(lambda s: len(s) >=5, strings))
print(data)
