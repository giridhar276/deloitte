

def display():
    return "python"

out = display()
print(out)


#generator 
#A normal function uses return and finishes 
# A generator function  uses yield and pauses remembering its state.
# next time you ask for a value, it continues from where it stopped

def gennumbers():
 yield 1
 yield 2 
 yield 3


g = gennumbers()
print(next(g))
print(next(g))
print(next(g))



####  without generator
r = range(1,100000)


#### with generator 
r = range(1,1000)
it = iter(r)
print(next(it))
print(next(it))





