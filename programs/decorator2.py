
import time 
import os
def timer(fn):
    def wrapper(*args,**kwargs):
        start = time.time()
        out = fn(*args, **kwargs)
        end = time.time()
        ms = (end - start) * 1000
        print("Total time taken :", round(ms,2),"ms")
        return out
    return wrapper

@timer 
def work():
    s = 0
    for i in range(1000000):
        s+=i 
    return s


@timer
def listfiles():
    files = [file for file in os.listdir()]
    return "Total no.of fiels :" + str(len(files))

print("display total time for iteration")
work()


print()
print("displaying file for listing files")
listfiles()