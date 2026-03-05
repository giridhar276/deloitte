#write a progra to read employee_info.csv and display all the UNIQUE workclasses 
import csv
try:      
    workset = set()
    with open("employee_info.csv") as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            workclass = line[1].strip()
            workset.add(workclass)
        
        for work in workset:
            print(work)
except Exception as err:
    print(err)
######################################################################
try:      
    workdict = dict()
    with open("employee_info.csv") as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            workclass = line[1].strip()
            workdict[workclass] = 1   # {'public':1 , "private":1}     
        for work in workdict:
            print(work)
except Exception as err:
    print(err)