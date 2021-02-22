class parent:
    def m1(self):
        print("inside m1")

class subchild(parent):
    def m2(self):
        print("inside m2")

class child(subchild):
    def m3(self):
        print("inside m3")


ch=child()
ch.m3()
ch.m2()
ch.m1()

ch1=subchild()

ch1.m2()
ch1.m1()







