# fixed arguments 
def display(a,b):
    print(a,b)
display(10,20)

# default arguments 
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display()
display(10)
display(10,20)
display(10,20,30)

# keyword arguments
def display(c,a,b):
    print(a,b,c)
display(b = 20,c = 30 , a = 10)

# variable length aruments # *args acts like a tuple
def display(*args):
    for val in args:
        print(val)
display(10,20,30,40,50,60,12,23,34,45,56,67,45,67,45,45,43,5,3,4,65,43)
