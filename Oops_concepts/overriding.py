class person(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name


    def __str__(self):
        return self.name+str(self.age)

p=person(24,'john')
p1=person(23,'kim')
print(p)
print(p1)