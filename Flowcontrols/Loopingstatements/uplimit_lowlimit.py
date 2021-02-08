num = int(input("enter the number:"))
lower = int(input("enter the lower limit value:"))
upper = int(input("enter the upper limit value:"))
for i in range(1, (upper + 1)):
    if i ** num in range(lower, upper):
        print(i ** num)


