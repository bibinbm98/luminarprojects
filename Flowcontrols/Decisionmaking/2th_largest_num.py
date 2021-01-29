num1 = int(input("enter the 1 num:"))
num2 = int(input("enter the 2 num:"))
num3 = int(input("enter the 3 num:"))
if (num1 > num2) & (num1 > num3):#----------->num1 is largest
    if num2 > num3:#------------------------->num2 is largest
        print(num2, "is second largest")
    else: #----------------------------------->num3 is largest
        print(num3, "is second largest")
elif (num2 > num1) & (num2 > num3):#--------->num2 is largest
      if num1 > num3:#----------------------->num1 is largest
        print(num1, "is second largest")
      else:#----------------------------------->num3 is largest
        print(num3, "is second largest")
elif (num3 > num1) & (num3 > num2):#--------->num3 is largest
     if num1 > num2:#------------------------->num1 is largest
        print(num1, "is second largest")
     else:#----------------------------------->num2 is largest
        print(num2, "is second largest")
