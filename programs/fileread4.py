
import csv
try:      
    mcount = 0
    fcount = 0
    with open("employee_info.csv") as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            gender = line[9].strip()
            if gender == "Male":
                mcount =mcount + 1
            if gender == "Female":
                fcount = fcount + 1
        print("Male count  :",mcount)
        print("Female count:", fcount)
except Exception as err:
    print(err)