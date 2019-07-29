class InstanceCounter():
    count = 0
    def __init__(self, val):
        self.val = val
        InstanceCounter.count +=1
    def set_val(self, newval):
        self.val = newval
    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print ("val of obj %s" % (obj.get_val()))
    print("count: %s" % (obj.get_count()))

