class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name


p = person(23, "john")
p1 = person(33, "jimmy")
p2 = person(44, "tom")

employee = []
employee.append(p)
employee.append(p1)
employee.append(p2)

for emp in employee:
    if emp.age > 25:
        print(emp.name)

empl = []
for emp in employee:
    empl.append(emp.age)
print(max(empl))
