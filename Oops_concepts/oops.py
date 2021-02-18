class person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)

obj=person()
obj.set_person(23,'john')
obj.print_person()

