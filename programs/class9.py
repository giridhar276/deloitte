class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1


    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print("value of obj: {}".format(obj.get_val()))
    print("Count : {}".format(obj.get_count())) #3
    

