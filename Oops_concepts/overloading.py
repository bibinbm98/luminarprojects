class maths:
    def add(self):
        print("inside no arg math method")

    def add(self, num1):
        print("in 1 args math method")

    def add(self, num1, num2):
        print(num1,num2,"in 2 args math method")


mat = maths()
mat.add(12,33)


class parent:
    def phone(self):
        print("nokia")

class child(parent):
    def phone(self):
        print("iphone")


ch=child()
ch.phone()
