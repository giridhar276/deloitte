
### duck typing : python does not care what the objects class is
#                 If only cares whether the object has the required method or behavior 
# python does not check whether the object is pycharm or vscode.
#  If only checks whether the object has method or not

# IDE class 1
class PyCharm:
    def execute(self):
        print("Running code in PyCharm IDE")

# IDE class 2
class VSCode:
    def execute(self):
        print("Running code in VS Code IDE")

# Programmer expects an object that has 'execute' method
class Programmer:
    def code(self, ide):
        ide.execute()

# Create instances
ide1 = PyCharm()
ide2 = VSCode()

# Pass different ide objects
p = Programmer()
p.code(ide1)
p.code(ide2)


