class student:
    def set_stud(self,rol,name,total):
        self.rol=rol
        self.name=name
        self.total=total
    def print_stud(self):
        print(self.rol)
        print(self.name)
        print(self.total)


obj=student()
obj.set_stud('001','bibin',100)
obj.print_stud()

