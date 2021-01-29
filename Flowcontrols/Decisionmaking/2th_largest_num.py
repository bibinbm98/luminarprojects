num1 = int(input("enter the 1 num:"))
num2 = int(input("enter the 2 num:"))
num3 = int(input("enter the 3 num:"))
if (num1 > num2) & (num1 > num3):
    if (num2 > num3):
        print(num2, "second")
    else:
        print(num3, "is second")
elif (num2 > num1) & (num2 > num3):
    if num1 <= num3:
        print(num1, "second")
    else:
        print(num3, "second")
elif (num3 > num1) & (num3 > num2):
    if (num1 > num2):
        print(num1, "seccond")
    else:
        print(num2, "second")
