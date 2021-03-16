lst=[10,20,30,40]
pos=int(input("enter the position"))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)

print("hello world")