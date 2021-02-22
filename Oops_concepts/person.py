class Employee:
    company_name="luminar technolab"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def person(self):
        print(self.name)
        print(self.age)
        print(Employee.company_name)

emp=Employee("BIBIN",22)
print(emp.name)
print(emp.age)
print(Employee.company_name)