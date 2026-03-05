
# method1
with open("employee_info.csv","r") as fobj:
    for line in fobj:
        print(line)

# method2
with open("employee_info.csv","r") as fobj:
    print(fobj.readlines()) # will display all the lines in list


# method3
with open("employee_info.csv","r") as fobj:
    print(fobj.read())       #  output will be in a single string

#method4
import csv 
with open("employee_info.csv","r") as fobj:
    # converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        print(line)


# method5
import pandas as pd 
df = pd.read_csv("employees_info.csv")
print(df)

