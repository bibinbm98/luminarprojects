class employee:
    def __init__(self, eid, name, desig, sal, exp):
        self.eid = eid
        self.name = name
        self.desig = desig
        self.sal = sal
        self.exp = exp

    def __str__(self):
        return self.name+" "+self.desig+" "+str(self.sal)


f = open("employee",'r')
employees=[]
for line in f:
    eid,name,desig,sal,exp=line.rstrip("\n").split(",")
    employees.append(employee(eid,name,desig,sal,exp))

for emp in employees:
    print(emp)

s=[]
for emp in employees:
    s.append(emp.sal)
print(max(s))

