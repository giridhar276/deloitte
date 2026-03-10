
import csv
import os 
class ClassOperations:
    def __init__(self,filename):
        self.filename = filename 
    def readFile(self):
        with open(self.filename,"r") as self.fobj:
            for line in self.fobj:
                print(line)

if __name__ == "__main__":
    f = "employee_info.csv"
    if os.path.isfile(f):
        file = ClassOperations(f)
        file.readFile()
