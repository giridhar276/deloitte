



import os 


def displayfiles():
    for file in os.listdir():
        print(file)

def displaysize():
    for file in os.listdir():
        print(file, os.path.getsize(file))   

if __name__ == "__main__":
    displayfiles()
    displaysize()

# this program executes in 2 different ways

# when this program is called directly ...        __name__ == "__main__"  will be True
# when this program is imported to other program  __name__ == "__main__"  becomes False